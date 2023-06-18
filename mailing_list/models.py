from django.db import models
from django.conf import settings

class Subscriber(models.Model):
    email = models.EmailField(max_length=254, primary_key=True)
    epoch = models.DateField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email'],
                name="one_row_per_email"
            )
        ]