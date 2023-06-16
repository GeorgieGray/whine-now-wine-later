from django.db import models
from django.contrib.auth.models import User
from checkout.models import Purchase
from product.models import Product

class Membership(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()