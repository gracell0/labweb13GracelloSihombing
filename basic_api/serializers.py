from rest_framework import serializers
from basic_api.models import DRFPost, Book

class DRFPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRFPost
        fields = '__all__'
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'rating', 'cover', 'uploaded']