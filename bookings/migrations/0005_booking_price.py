# Generated by Django 4.2.17 on 2025-01-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_remove_booking_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]