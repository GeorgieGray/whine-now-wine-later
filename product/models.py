from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.FloatField()
    code = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True)
    stripe_price = models.CharField(max_length=64)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return "Product: " + self.name

class Workout(models.Model):
    WORKOUT_TYPES = [
        ("a", "Endurance"),
        ("b", "Powerlifting"),
        ("c", "Spin Indoor Cycling"),
        ("d", "Flexibility")
    ]
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    day = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    type = models.CharField(max_length=1, choices=WORKOUT_TYPES)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'day', 'time', 'type'],
                name="one_class_per_slot_per_user"
            )
        ]