# Generated by Django 5.1.3 on 2024-11-15 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0006_meal_hostel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='hostel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='hostelapp.hostel'),
        ),
    ]
