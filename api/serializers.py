from rest_framework.serializers import ModelSerializer
from api.models import Book, Athenaeum


class BookSerializer(ModelSerializer):
    """Книги."""

    class Meta:
        model = Book
        fields = '__all__'


class AthenaeumSerializer(ModelSerializer):
    """Библиотеки."""

    class Meta:
        model = Athenaeum
        fields = '__all__'
