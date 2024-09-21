from .models import patientdata
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("login",views.loginpage,name="login"),
    path("doctor",views.doctorpage,name="doctor"),
    path('show-details',views.show_details,name="show-details"),
    path("add_details",views.add_details,name="add_details"),
    path("edit_details/<int:pk>",views.edit_details,name="edit"),
    path('register/',views.registerpage,name="register")
]
