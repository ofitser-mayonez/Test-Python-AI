from rest_framework.viewsets import ModelViewSet

from api.models import Athenaeum, Book
from api.serializers import AthenaeumSerializer, BookSerializer


class BookViewSet(ModelViewSet):
    """ViewSet книг."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AthenaeumViewSet(ModelViewSet):
    """ViewSet библиотек."""

    queryset = Athenaeum.objects.all()
    serializer_class = AthenaeumSerializer
