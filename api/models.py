from django.db import models

from api.constants import ATHENAEUM_NAME_LENGTH, BOOK_NAME_LENGTH


class Book(models.Model):
    """Модель книг."""

    name = models.CharField(
        max_length=BOOK_NAME_LENGTH,
        verbose_name='Название книги'
    )

    def __str__(self):
        return self.name


class Athenaeum(models.Model):
    """Модель библиотек."""

    name = models.CharField(
        max_length=ATHENAEUM_NAME_LENGTH,
        verbose_name='Название библиотеки'
    )
    book = models.ManyToManyField(
        Book,
        through='BookAthenaeum',
    )

    def __str__(self):
        return self.name


class BookAthenaeum(models.Model):
    """Модель связи книг и библиотек."""

    athenaeum = models.ForeignKey(
        Athenaeum, on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество книг'
    )
