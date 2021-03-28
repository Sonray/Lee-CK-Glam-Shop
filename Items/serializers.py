from rest_framework import serializers
from .models import Product_details, Reviews
from django.utils import timezone


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_details
        fields = '__all__'
        depth = 1
        
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
        depth = 1