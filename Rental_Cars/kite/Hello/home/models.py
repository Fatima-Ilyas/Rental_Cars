from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email =  models.CharField(max_length=122)
    subject = models.CharField(max_length=200)
    message = models.TextField()

class booking(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    number = models.CharField(max_length=12)
    fdate = models.DateField()
    tdate = models.DateField()
    car = models.CharField(max_length=122)
   
    
    