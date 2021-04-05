from rest_framework import serializers
from .models import Product_details, Reviews
from django.utils import timezone
from  Authentication.models import  Account


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product_details
        exclude = ('admin_id',)
        depth = 1
        
        
        
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
        depth = 1
        
    def validate(self, attrs):
        user_id = attrs.get('user_id', '')
        if Account.objects.filter(id=attrs['user_id']).exists():
            raise serializers.ValidationError({'user_id',('Please register as a user to leave a review')})
        
        return super().validate(attrs)
    def validate(self, data):
        return data
        
    def create(self, validated_data):
        review = Reviews.objects.create_user(**validated_data)
        return review

    def __str__(self):
        return Reviews