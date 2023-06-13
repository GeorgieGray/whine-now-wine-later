from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name= models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=32)

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.FloatField()
    code = models.CharField(max_length=32, unique=True)
