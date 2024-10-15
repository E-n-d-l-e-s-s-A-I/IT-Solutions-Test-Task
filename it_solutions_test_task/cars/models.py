from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

from .validators import validate_car_year

User = get_user_model()


class CreatedAt(models.Model):
    created_at = models.DateTimeField(
        'Дата и время создания ',
        auto_now_add=True)

    class Meta:
        abstract = True


class Car(CreatedAt):
    make = models.CharField('Марка автомобиля', max_length=100)
    model = models.CharField('Модель автомобиля', max_length=100)
    year = models.PositiveIntegerField(
        'Год выпуска',
        blank=True,
        null=True,  # исходя из тестовых данных в тз
        help_text='Год выпуска должен быть не раньше 1885, '
                  'может быть не указан',
        validators=[validate_car_year],
    )
    description = models.TextField('Описание')
    updated_at = models.DateTimeField(
        'Дата и время последнего изменения',
        auto_now=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cars',
        verbose_name='Автор',
    )

    @property
    def name(self):
        return f'{self.make} {self.model}'

    class Meta():
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'Автомобиль {self.make} {self.model}, id: {self.pk}'

    def get_absolute_url(self):
        return reverse_lazy("cars:car_detail", kwargs={"pk": self.pk})


class Comment(CreatedAt):
    content = models.TextField('Содержание комментария')
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Автомобиль",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )

    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created_at',)

    def __str__(self):
        return (f'Комментарий id: {self.pk}, '
                f'пользователя {self.author.username}')

# В тестовом задании не был уточнен,
# способ восстановления ссылочной целостности бд

# Так же, не была уточнена максимальная длина текстовых полей

# Эти параметры были выбраным мной самостаятельно,
# учитывая специфику предметной области
