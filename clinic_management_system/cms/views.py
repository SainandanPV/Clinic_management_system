from django.shortcuts import render,redirect,get_object_or_404
import uuid
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . models import patientdata
from .forms import patientform,CustomUserRegistrationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def home(request):
         return render(request,'patient.html')

def registerpage(request):
        
        if request.method=='POST':
                form=CustomUserRegistrationForm(request.POST)
                if form.is_valid():
                        form.save()
                        messages.success(request,'Account created successfully!')
                        return redirect('login')
                else:
                        print(form.errors)
        else:
                form=CustomUserRegistrationForm()       
        return render(request,'register.html',{'form':form})

def loginpage(request):
        if request.method=='POST':
                username=request.POST.get('username')
                password=request.POST.get('password')
                user=authenticate(request,username=username,password=password)
                if user is not None:
                        login(request,user)
                        return redirect('doctor')
                else:
                        messages.info(request,'Username or Password is incorrect')
                       
        return render(request,'login.html')

def doctorpage(request):
        return render(request,'doctor.html')


def show_details(request):
        if request.POST:
                patient_id = request.POST.get('cardno')

                if patient_id:
                        try:
                                
                                patient=patientdata.objects.get(id=patient_id)
                                return render(request,'details.html',{'patient':patient})
                        except patientdata.DoesNotExist: 
                                messages.error(request,"Patient data does not exist !!")
                else:
                        messages.error(request,"No patient ID Provided")
        return render(request,'doctor.html')
                        
def add_details(request):
        context={}
        if request.POST:
                
                form=patientform(request.POST)
                if form.is_valid():
                        print("Form is Valid, saving data")
                        form.save(commit=True)
                        return redirect('doctor')
                else:
                        print("Form is invalid",form.errors)
                        context['form']=form
        else:
                form=patientform()
                context['form']=form
        return render(request,"addnew.html",context)


def edit_details(request,pk):
        obj=get_object_or_404(patientdata,pk=pk)
        if request.POST and 'edit' in request.POST:
                
                form=patientform(request.POST,instance=obj)

                if form.is_valid():
                        form.save()
                        return redirect('doctor')
        else:
                form=patientform(instance=obj)

        return render(request,'edit_template.html',{'form':form,'patient':obj})

