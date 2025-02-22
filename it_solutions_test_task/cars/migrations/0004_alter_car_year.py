# Generated by Django 4.2.16 on 2024-10-14 05:27

import cars.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(blank=True, help_text='Год выпуска должен быть не раньше 1885, может быть не указан', null=True, validators=[cars.validators.validate_car_year], verbose_name='Год выпуска'),
        ),
    ]
