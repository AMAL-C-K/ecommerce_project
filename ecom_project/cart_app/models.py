import django
from django.utils import timezone
from django.db import models
from ecom_app.models import Products
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def total(self):
        return self.product.price * self.quantity  
      

class Checkout(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  
    amount = models.CharField(max_length=150)
    product_name = models.CharField(max_length=255, null=True)
    payment_id = models.CharField(max_length=150)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.cart.product.name