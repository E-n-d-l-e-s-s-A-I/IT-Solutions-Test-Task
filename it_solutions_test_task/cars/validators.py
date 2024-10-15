from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_car_year(value):
    current_year = timezone.now().year
    first_car_year = 1885  # The first car was produced in 1885

    if value < first_car_year or value > current_year:
        raise ValidationError(f'Year must be between 1885 and {current_year}.')
