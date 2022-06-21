from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
# Create your models here.

class CustomerUser(AbstractUser):
    phone_number = models.CharField(max_length=10,default="")
    address = models.CharField(default="", max_length=255)
    avatar = models.ImageField(upload_to='images',default=None,null=False)
    
    def __str__(self):
        return self.username
    class Meta:
        permissions = permissions = [('can_view_category', 'can_view_category'),
                                    ('can_change_order', 'can_change_order'),
                                    ('can_view_product', 'can_view_product'),
                                    ('can_view_variation', 'can_view_variation'),
                                    ('can_change_user', 'can_change_user'),
                                    ('can_add_order', 'can_add_order'),
                                    ('can_delete_order', 'can_delete_order'),
                                    ('can_view_order', 'can_view_order'),
                                    ('can_add_cart', 'can_add_cart'),
                                    ('can_change_cart', 'can_change_cart'),
                                    ('can_delete_cart', 'can_delete_cart'),
                                    ('can_view_cart', 'can_view_cart'),
                                    ('can_add_cart_item', 'can_add_cart_item'),
                                    ('can_change_cart_item', 'can_change_cart_item'),
                                    ('can_delete_cart_item', 'can_delete_cart_item'),
                                    ('can_view_cart_item', 'can_view_cart_item'),
                                    
                                    ('can_add_message', 'can_add_message'),
                                    ('can_change_message', 'can_change_message'),
                                    ('can_delete_message', 'can_delete_message'),
                                    ('can_view_message', 'can_view_message'),
                                    ('can_add_order_detail', 'can_add_order_detail'),
                                    ('can_change_order_detail', 'can_change_order_detail'),
                                    ('can_delete_order_detail', 'can_delete_order_detail'),
                                    ('can_view_order_detail', 'can_view_order_detail')]
