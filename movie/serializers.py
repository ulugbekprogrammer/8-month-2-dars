from django.db.models import fields
from rest_framework import serializers
from .models import Book
 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'author', 'description')