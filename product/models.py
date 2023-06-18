from django.db import models
from django.conf import settings

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
    WORKOUT_TIMES = [
        ("01", "1am"),
        ("02", "2am"),
        ("03", "3am"),
        ("04", "4am"),
        ("05", "5am"),
        ("06", "6am"),
        ("07", "7am"),
        ("08", "8am"),
        ("09", "9am"),
        ("10", "10am"),
        ("11", "11am"),
        ("12", "12pm"),
        ("13", "1pm"),
        ("14", "2pm"),
        ("15", "3pm"),
        ("16", "4pm"),
        ("17", "5pm"),
        ("18", "6pm"),
        ("19", "7pm"),
        ("20", "8pm"),
        ("21", "9pm"),
        ("22", "10pm"),
        ("23", "11pm"),
        ("24", "12am")
    ]
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    day = models.DateField(auto_now=False, auto_now_add=False)
    time = models.CharField(max_length=2, choices=WORKOUT_TIMES)
    type = models.CharField(max_length=1, choices=WORKOUT_TYPES)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'day', 'time'],
                name="one_class_per_slot_per_user"
            )
        ]
        ordering = ["day", "time"]

    def type_verbose(self):
        return dict(Workout.WORKOUT_TYPES)[self.type]

    def time_verbose(self):
        return dict(Workout.WORKOUT_TIMES)[self.time]