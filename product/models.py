from tkinter import TRUE
from django.db import models

from user.models import CustomerUser

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    active = models.BooleanField()
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    product_img = models.CharField(max_length=1000, blank=True,null=True )
    image_view = models.ImageField(upload_to='images',default=None,null=False)
    def __str__(self):
        return self.title
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Message(models.Model):
    product = models.ForeignKey(Product, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.message