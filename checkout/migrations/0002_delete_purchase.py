# Generated by Django 4.0 on 2023-06-18 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_delete_membership'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
