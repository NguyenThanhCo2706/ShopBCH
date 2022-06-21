from pyexpat import model
from django.db import models
from  user.models import CustomerUser
from product.models import Product
from cart.models import Cart
# Create your models here.
class Order(models.Model):
    user = models.IntegerField(null = False)
    phone_number = models.CharField(max_length=10,default="")
    name_receive = models.CharField(default="", max_length=255)
    shipping_address = models.CharField(max_length=255, default='', null=False)
    total_price = models.FloatField(default=0)
    order_description = models.TextField(default='', null=False)
    is_delivered = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.phone_number

class OrderDetail(models.Model):
    order_id = models.IntegerField(null = False)
    pro_name = models.CharField(max_length=255)
    money = models.IntegerField(null = False, default=0)
    amount = models.IntegerField(default=1, null=False)
    total_money = models.FloatField(default=0)
    address_delivery = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)