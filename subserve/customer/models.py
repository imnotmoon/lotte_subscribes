from django.db import models
from django.contrib.auth.models import User
from store.models import Store
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Manager(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    store = models.OneToOneField(Store, on_delete=models.CASCADE, null=True)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=45, null=True)
    phone=models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=45, null=False, default="admin@subserve.com")
    password = models.CharField(max_length=15, null=False, default="qweqwe123")

    def __str__(self) :
        return str(self.store.storename) + " - " + self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=45, null=True)
    phone=models.CharField(max_length=45, null=True)
    marketing_email=models.BooleanField(null= True)   
    marketing_sms=models.BooleanField(null= True)
    barcode=models.IntegerField(null= True)
    purchasing_type=models.IntegerField(null=True)
    auto_extension=models.BooleanField(null = True)
    locality=models.IntegerField(null = True)
    recent_search_keywords=models.CharField(max_length=45, null=True)
    recent_viewed=models.CharField(max_length=45, null=True)
    profile=models.ImageField(upload_to="", height_field=None, width_field=None, default='')
    address=models.CharField(max_length=45)
    birthday=models.DateTimeField()
    sex=models.BooleanField(null = True)
    certified=models.BooleanField(null = True)

    def __str__(self) :
        return str(self.id) + " " + self.name


# 아직 마이그레이션 안함
