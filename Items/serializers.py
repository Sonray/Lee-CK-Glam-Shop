from rest_framework import serializers
from .models import Product_details, Reviews, Order
from django.utils import timezone
from  Authentication.models import  Account
from django.views.generic import CreateView
from rest_framework.response import Response


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product_details
        exclude = ('admin_id',)
        depth = 1
                
class OrderSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Order
        fields = '__all__'
    
    def create(self,request, MerchantRequestID1, CheckoutRequestID1,*args,**kwargs):
        
        data = request.data
        new_order = Order.objects.create( user_id = Account.objects.get(id=data["user_id"]), product = Product_details.objects.get(id=data["product"]) , first_name = data["first_name"], last_name = data["last_name"], phone_number = data["phone_number"],
                                            order_phone_number =data["order_phone_number"], delivery_address = data["delivery_address"], region = data["region"], city = data["city"], delivery_method = data["delivery_method"],
                                            price =data["price"], CheckoutRequestID = CheckoutRequestID1, MerchantRequestID = MerchantRequestID1
                                            )
                                        
        
        new_order.save()
        serializer = OrderSerializer(new_order)
        return Response (serializer.data)
                
        
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
    
class MpesaSerializer(serializers.ModelSerializer):
        
    class Meta:
        # model = Order_Made_by_Mpesa
        fields = "__all__"
        
    
    def validate(self, data):
        return data
    
        # def create(self,request,*args,**kwargs):
            
        #     data = request.data
            
        #     new_review = Reviews.objects.create( product = Product_details.objects.get(id=data["product"]),
        #                                         user_id = Account.objects.get(id=data["user_id"]), 
        #                                         Product_review=data["Product_review"], 
        #                                         product_rating=data["product_rating"] )
            
        #     new_review.save()
        #     serializer = ReviewSerializer(new_review)
        #     return Response (serializer.data)

    # def __str__(self):
    #     return Order_Made_by_Mpesa
    