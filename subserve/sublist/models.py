from django.db import models
from store.models import Store
from menu.models import Menu
from customer.models import Customer
from django.contrib.auth.models import User

class Subscribes(models.Model):
     id = models.AutoField(primary_key = True)
     user_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
     store_id=models.ForeignKey(Store, on_delete=models.CASCADE)
     menu_id=models.ForeignKey(Menu, on_delete=models.CASCADE)
     start_date=models.DateTimeField(auto_created=True)   
     end_date=models.DateTimeField(auto_created=True)
     total=models.IntegerField(null= True)
     cycle=models.IntegerField(null= True)
     remain=models.IntegerField(null= True)
     last_used=models.DateTimeField(auto_created=True,null=True)
     purchased=models.DateTimeField(auto_created=True, null= True)
     purchased_type=models.IntegerField(null= True)

     def __str__(self) :
          return str(self.user_id) + "-" + str(self.store_id) + "-" + str(self.menu_id)