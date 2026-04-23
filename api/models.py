from django.db import models

from api.constants import (BOOK_NAME_LENGTH, ATHENAEUM_NAME_LENGTH)


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
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='books'
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество книг'
    )

    def __str__(self):
        return self.name
