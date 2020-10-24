from django.db import models
from django.contrib import admin

# Create your models here.
class Store(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #objects = models.Manager()
    id=models.AutoField(primary_key=True)
    storename = models.CharField(max_length=45, null = True)
    longitude=models.DecimalField(max_digits=30, decimal_places=20, null = True)
    latitude=models.DecimalField(max_digits=30, decimal_places=20, null = True)
    address=models.CharField(max_length=45, null = True)
    photo=models.ImageField(upload_to="", height_field=None, width_field=None, default='')
    subscribers=models.IntegerField(null = True)
    rank=models.IntegerField(null = True)
    is_premium=models.BooleanField(null = True)
    description=models.CharField(max_length=45, null=True)
    sns1=models.CharField(max_length=45, null=True)
    sns2=models.CharField(max_length=45, null=True)
    phone=models.CharField(max_length=45, null = True)
    running_time=models.CharField(max_length=45, null = True)
    break_time=models.CharField(max_length=45, null = True)
    closed_on=models.CharField(max_length=15, null = True)
    num_menu=models.IntegerField(null = True)
    locality=models.IntegerField(null = True)
    comment=models.CharField(max_length=45, null = True)
    category=models.IntegerField(null = True)

    def __str__(self):
       return self.storename
