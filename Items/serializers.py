from rest_framework import serializers
from .models import Product_details, Reviews, Order, Ordered_Items, Customer_Pickup_point
from  Authentication.models import  Account
from rest_framework.response import Response


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product_details
        exclude = ('admin_id',)
        depth = 1

class OrderedItemSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Ordered_Items
        fields = '__all__'

    
class CustomerPickupSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Customer_Pickup_point
        fields = '__all__'
    
        
class OrderSerializer(serializers.ModelSerializer):
    
    orderitems      = OrderedItemSerializer(many=True)
    customerpick    = CustomerPickupSerializer(many=True)
    
    class Meta:
        model = Order
        fields = [
            'user_id',
            'payment_id',
            'amount_paid',
            'Payment_method',
            'delivery_method',
            'orderitems',
            'customerpick',
            ]
    
    
class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reviews
        fields = "__all__"
        depth = 1
        
    
    def validate(self, data):
        return data
    
    def create(self,request,*args,**kwargs):
        
        data = request.data
        
        new_review = Reviews.objects.create( product = Product_details.objects.get(id=data["product"]),
                                            user_id = Account.objects.get(id=data["user_id"]), 
                                            Product_review=data["Product_review"], 
                                            product_rating=data["product_rating"] )
        
        new_review.save()
        serializer = ReviewSerializer(new_review)
        return Response (serializer.data)

    def __str__(self):
        return Reviews
    
  