from rest_framework.serializers import ModelSerializer
from .models import Book, Shelf

class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

