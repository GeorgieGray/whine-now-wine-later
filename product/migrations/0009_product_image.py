# Generated by Django 4.0 on 2023-06-19 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_workout_one_class_per_slot_per_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]
