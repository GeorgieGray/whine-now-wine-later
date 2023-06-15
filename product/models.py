from django.db import models

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.FloatField()
    code = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Product: " + self.name
