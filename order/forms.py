from pyexpat import model
from django import forms
from numpy import product
from .models import Order, OrderDetail
from user.models import CustomerUser
from product.models import Product
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widget ={
                user:= forms.ModelChoiceField(
                    queryset = CustomerUser.objects.all(), 
                    label="User",
                    widget=forms.Select(
                                attrs={
                                    'placeholder': 'CustomerUser', 'class': 'form-control'}),
                                required=True
                    )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['style'] = 'width:100px !important;'
        self.fields['name_receive'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['shipping_address'].widget.attrs.update({'class': 'form-control'})
        self.fields['order_description'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_completed'].widget.attrs.update({'class': 'form-check-input'})

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = "__all__"
        widget ={
                order:= forms.ModelChoiceField(
                    queryset = Order.objects.all(), 
                    label="Order",
                    widget=forms.Select(
                                attrs={
                                    'placeholder': 'Order', 'class': 'form-control'}),
                                required=True
                    ),
                product:= forms.ModelChoiceField(
                    queryset = Product.objects.all(), 
                    label="Product",
                    widget=forms.Select(
                                attrs={
                                    'placeholder': 'Product', 'class': 'form-control'}),
                                required=True
                    )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_id'].widget.attrs['style'] = 'width:100px !important;'
        self.fields['pro_id'].widget.attrs['style'] = 'width:100px !important;'
        self.fields['number'].widget.attrs.update({'class': 'form-control'})
        self.fields['address_delivery'].widget.attrs.update({'class': 'form-control'})
