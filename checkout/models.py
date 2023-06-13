from django.db import models
from product.models import Product

class Purchase(models.Model):
    PAYMENT_METHODS = [
        ("C", "Credit Card"),
        ("B", "Bitcoin")
    ]
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    paid = models.FloatField()
    payment_method = models.CharField(max_length=1, choices=PAYMENT_METHODS)