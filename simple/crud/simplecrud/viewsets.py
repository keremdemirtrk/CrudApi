from rest_framework import viewsets
from . import models
from . import serializers


class BookViewset(viewsets.ModelViewSet):
    queryset = models.BookModel.objects.all()
    serializer_class = serializers.BookSerializer
