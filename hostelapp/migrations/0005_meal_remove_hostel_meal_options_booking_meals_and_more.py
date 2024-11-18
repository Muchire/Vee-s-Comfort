# Generated by Django 5.1.3 on 2024-11-15 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0004_mealoption_hostel_meal_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='meal_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='meal_options',
        ),
        migrations.AddField(
            model_name='booking',
            name='meals',
            field=models.ManyToManyField(blank=True, to='hostelapp.meal'),
        ),
        migrations.DeleteModel(
            name='MealOption',
        ),
    ]