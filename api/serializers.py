from django.db.models import Sum
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from api.models import Athenaeum, Book, BookAthenaeum


class BookSerializer(ModelSerializer):
    """Книги."""

    percentage_ratio = SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"

    def get_percentage_ratio(self, obj):

        # Общее количество конкретной книги во всех библиотеках
        total_book = BookAthenaeum.objects.filter(
            book=obj
        ).aggregate(Sum("quantity"))[
            "quantity__sum"
        ]
        result = {}

        # Количество конкретной книги в каждой библиотеке
        for athenaeum in Athenaeum.objects.all():

            total_book_athenaeum = BookAthenaeum.objects.filter(
                book=obj, athenaeum=athenaeum
            ).aggregate(Sum("quantity"))["quantity__sum"]

            if total_book_athenaeum:

                # Соотношение общего количества к каждой библиотеке
                result[athenaeum.name] = (
                    f'{total_book_athenaeum} '
                    f'{(round((total_book_athenaeum / total_book) * 100))}%'
                )

            else:
                result[athenaeum.name] = 0

        return result


class AthenaeumSerializer(ModelSerializer):
    """Библиотеки."""

    class Meta:
        model = Athenaeum
        fields = "__all__"
