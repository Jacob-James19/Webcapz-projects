from django import forms
from .models import Product, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "address", "phone"]