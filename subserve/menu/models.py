from django.db import models
from django.contrib.auth.models import User
from store.models import Store
# Create your models here.

class Menu(models.Model):
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE)
    menu_id=models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=20, default='')
    description=models.CharField(max_length=45, default='')
    price=models.IntegerField(null = True)
    photo=models.ImageField(upload_to="", height_field=None, width_field=None, default='')
    allergic=models.CharField(max_length=45, null = True)
    subscribers=models.IntegerField(null = True)
    cycle=models.IntegerField(null = True)
    count=models.IntegerField(null = True)
    last_subscribers=models.IntegerField(null = True)
    discount=models.IntegerField(null = True)
    in_event=models.BooleanField(null = True)

    def __str__(self) :
        return str(self.store_id) + " -- " + self.menu_name
      
