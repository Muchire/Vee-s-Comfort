# Generated by Django 5.1.3 on 2024-11-16 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0009_remove_booking_airport_pickup_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='meals',
            field=models.ManyToManyField(related_name='bookings', to='hostelapp.meal'),
        ),
    ]
