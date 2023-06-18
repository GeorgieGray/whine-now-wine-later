from django.db import models
from django.conf import settings

class Subscriber(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    epoch = models.DateField()