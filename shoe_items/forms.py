# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Message, Product, brands, categories
from django.core.validators import RegexValidator

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'brands', 'image_path', 'price', 'small_images', 'colors', 'sizes', 'categories', 'discount', 'discount_percent']


class RegisterForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format : '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)
    email = forms.EmailField()
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone']