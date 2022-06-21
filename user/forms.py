from django import forms
from .models import CustomerUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomerUser
        fields = ('username', 'password', 'email', 'phone_number', 'address', 'avatar')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['avatar'].widget.attrs.update({'class': 'form-control'})

class AdminForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'password')