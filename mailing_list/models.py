from django.db import models
from django.contrib.auth.models import User

class Subscriber(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    epoch = models.DateField()