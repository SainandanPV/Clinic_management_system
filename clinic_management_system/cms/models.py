from django.db import models,migrations
import uuid

class patientdata(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    lastvisit = models.DateField(auto_now=True)
    data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name