from django.db.models import fields
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Item
        fields = ('category', 'subcategory', 'name', 'amount', 'created_at', 'updated_at')