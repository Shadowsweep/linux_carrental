from django.db import models

# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=70, blank=False,default='')
    description = models.CharField(max_length=150, blank=False,default='')
    icon = models.ImageField(upload_to='static/')


class SubCategory(models.Model):

    cid = models.CharField(max_length=70, blank=False,default='')
    companyname = models.CharField(max_length=70, blank=False,default='')
    subcategoryname = models.CharField(max_length=70, blank=False,default='')
    description = models.CharField(max_length=150, blank=False,default='')
    icon = models.ImageField(upload_to='static/')

class Vehicle(models.Model):

    cid = models.CharField(max_length=70, blank=False,default='')
    sid = models.CharField(max_length=70, blank=False,default='')
    modelyear = models.CharField(max_length=70, blank=False,default='')
    price = models.CharField(max_length=70, blank=False,default='')
    insured = models.CharField(max_length=70, blank=False,default='')
    variant = models.CharField(max_length=70, blank=False,default='')
    registrationno = models.CharField(max_length=70, blank=False,default='')
    ownername = models.CharField(max_length=150, blank=False,default='')
    mobileno = models.CharField(max_length=70, blank=False,default='')
    color = models.CharField(max_length=70, blank=False,default='')
    fueltype = models.CharField(max_length=70, blank=False,default='')
    noofseats = models.CharField(max_length=70, blank=False,default='')
    transmissiontype = models.CharField(max_length=70, blank=False,default='')
    icon = models.ImageField(upload_to='static/')

   
class Administrator(models.Model):

    adminname = models.CharField(max_length=70, blank=False,default='')
    mobileno = models.CharField(max_length=150, blank=False,default='')
    emailid = models.CharField(max_length=150, blank=False,default='')
    password = models.CharField(max_length=150, blank=False,default='')

class AddVehicle(models.Model):
    
    brand = models.CharField(max_length=150, blank=False,default='')
    segment = models.CharField(max_length=150, blank=False,default='')
    model_name = models.CharField(max_length=150, blank=False,default='')
    price = models.CharField(max_length=70, blank=False,default='')
    # insured = models.CharField(max_length=70, blank=False,default='')
    # color = models.CharField(max_length=70, blank=False,default='')
    fueltype = models.CharField(max_length=70, blank=False,default='')
    noofseats = models.CharField(max_length=70, blank=False,default='')
    transmissiontype = models.CharField(max_length=70, blank=False,default='')
    icon = models.ImageField(upload_to='static/')
    usericon = models.ImageField(upload_to='static/')