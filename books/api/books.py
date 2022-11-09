from rest_framework import serializers, viewsets
from books.models import Books

class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

class GenreSerializer(serializers.Serializer):
    genre_name = serializers.CharField(max_length=255)

class PublishingHouseSerializer(serializers.Serializer):
    publishing_house_name = serializers.CharField(max_length=255)
    manager_first_name = serializers.CharField(max_length=255)
    manager_last_name = serializers.CharField(max_length=255)
    manager_email = serializers.CharField(max_length=255)

class BookSerializer(serializers.Serializer):
    class Meta: 
        model = Books

    name = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    number_in_stock = serializers.IntegerField()
    author = AuthorSerializer()
    genre = GenreSerializer()
    publishing_house = PublishingHouseSerializer()
        

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


