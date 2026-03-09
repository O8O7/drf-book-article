from rest_framework import viewsets

from sample_app.models import BookModel
from sample_app.serializers.book import BookSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BookModel.objects.order_by("id")
    serializer_class = BookSerializer
