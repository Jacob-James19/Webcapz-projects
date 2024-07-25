from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="products", null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=False, null=False)
    avaliability = models.BooleanField()

    def __str__(self):
        return self.name




class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)


    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    product = models.CharField(max_length=150)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

