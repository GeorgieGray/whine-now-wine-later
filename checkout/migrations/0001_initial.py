# Generated by Django 4.0 on 2023-06-13 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('paid', models.FloatField()),
                ('payment_method', models.CharField(choices=[('C', 'Credit Card'), ('B', 'Bitcoin')], max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]