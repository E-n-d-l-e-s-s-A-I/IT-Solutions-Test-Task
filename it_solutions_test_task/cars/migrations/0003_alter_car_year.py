# Generated by Django 4.2.16 on 2024-10-14 05:26

import cars.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_description_alter_car_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(help_text='Год выпуска должен быть не раньше 1885', null=True, validators=[cars.validators.validate_car_year], verbose_name='Год выпуска'),
        ),
    ]
