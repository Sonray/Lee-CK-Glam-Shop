from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Reviews, Product_details,Order, Ordered_Items, Customer_Pickup_point
from Authentication.models import  Account
from .serializers import ProductSerializer, ReviewSerializer, OrderSerializer, MpesaSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions, generics, status, filters
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
import requests
from .mpesa_payments import Lipa_na_mpesa
import json

# Create your views here.


@permission_classes((permissions.IsAuthenticated, TokenHasReadWriteScope))
class Display_all_products(APIView):
    
    def get(self, request, format=None):
        all_post = Product_details.objects.all()
        serializers = ProductSerializer(all_post, many=True)
        return Response(serializers.data)
        
        
@permission_classes((permissions.IsAuthenticated, TokenHasScope, TokenHasReadWriteScope ))
class Display_specific_product(APIView):
    
    def get_object(self,pk):
        '''
        retrieve product object from database
        '''

        try:
            return Product_details.objects.get(pk=pk)
        except Product_details.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''
        get a single product object with its details
        '''

        product=self.get_object(pk)
        serializers=ProductSerializer(product)
        return Response(serializers.data) 


@permission_classes((permissions.IsAuthenticated, TokenHasScope, TokenHasReadWriteScope))
class Make_a_review(APIView):    

    serializer_class = ReviewSerializer

    def post(self, request, format=None):
        
        review = request.data
        serializers = self.serializer_class(data=review)

        if serializers.is_valid(raise_exception=True):

            serializers.create(request)

            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.IsAuthenticated, TokenHasScope, TokenHasReadWriteScope )) 
class Display_all_Reviews(APIView):

    def get_object(self,pk):
        '''
        retrieve product object from database
        '''

        try:
            return Reviews.objects.filter(product=pk)
        except Reviews.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''
        get a single product object with its details
        '''

        review=self.get_object(pk)
        serializers=ReviewSerializer(review, many=True)
        return Response(serializers.data) 


@permission_classes((permissions.IsAuthenticated, TokenHasScope, TokenHasReadWriteScope )) 
class Search_products_category(generics.ListAPIView):
    queryset = Product_details.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['category__category']
    
    
@permission_classes((permissions.IsAuthenticated, TokenHasScope, TokenHasReadWriteScope)) 
class Search_products_subcategory(generics.ListAPIView):
    queryset = Product_details.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['sub_category__sub_category']
    
    
@permission_classes((permissions.IsAuthenticated, TokenHasScope, TokenHasReadWriteScope)) 
class Search_products(generics.ListAPIView):
    queryset = Product_details.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [ '^sub_category__sub_category', '^sub_category__sub_category',
                     '^product_description', '^product_name', 'new_price',
                     '^specifications__product_specification', '^key_features__product_feature' ]
    

@permission_classes((permissions.AllowAny,)) 
class  Order_Product_MPESA(APIView):
    
    serializer_class = OrderSerializer

    def post(self, request, format=None):
        
        review = request.data
        data = request.data
        serializers = self.serializer_class(data=review)

        if serializers.is_valid(raise_exception=True):
            
            phone_number = str( review['order_phone_number'])
            amount_1 = str(review['price'])
            
            mpesa_dict = Lipa_na_mpesa( phone_number, amount_1)
            
            ResultCode      = mpesa_dict['ResultCode']
            payment_id      = mpesa_dict['CallbackMetadata.Item[1].Value']
            Ordered_Item    = data['Ordered_Items']
            pickup_point    = data['Customer_Pickup_point']
            
            if ResultCode != 0:
                
                order = Order.objects.create(user_id=data['user_id'], payment_id = payment_id, amount_paid=data['amount_paid'],
                                    Payment_method='M-Pesa',delivery_method=data['delivery_method'] )
                
                order_id = order.pk
                
                for item in Ordered_Item:
                    
                    Ordered_Items.objects.create(order_id = order_id, product = mpesa_dict['product'], quantity = mpesa_dict['quantity'], price = mpesa_dict['price'])
                
                for pickup in pickup_point:
                    
                    Customer_Pickup_point.objects.create(order_id = order_id, user_id=data['user_id'],Station_id = data['Station_id'],
                                                        first_name=data['user_id'], last_name=data['last_name'], phone_number=data['phone_number'],
                                                        Delivery_address=data['Delivery_address'], County=data['County'], City=data['City'] )
                
            else:
                
                order = Order.objects.create(user_id=data['user_id'], payment_id = payment_id, amount_paid=data['amount_paid'],
                                    Payment_method='M-Pesa',delivery_method=data['delivery_method'], payment_status = True )
                
                order_id = order.pk
                
                for item in Ordered_Item:
                    
                    Ordered_Items.objects.create(order_id = order_id, product = data['product'], quantity = data['quantity'], price = data['price'])
                
                for pickup in pickup_point:
                    
                    Customer_Pickup_point.objects.create(order_id = order_id, user_id=data['user_id'],Station_id = data['Station_id'],
                                                        first_name=data['user_id'], last_name=data['last_name'], phone_number=data['phone_number'],
                                                        Delivery_address=data['Delivery_address'], County=data['County'], City=data['City'] )
                 
                
            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@permission_classes((permissions.AllowAny,)) 
class  Order_Product_Paypal(APIView):
    
    serializer_class = OrderSerializer

    def post(self, request, format=None):
                
        data = request.data
        serializers = self.serializer_class(data=data)
        
        PPClient = PayPalClient()
        
        body = json.loads(request.body)
        data = body["orderID"]
        user_id = request.user.id
        
        requestorder = OrdersGetRequest(data)
        response_data = PPClient.client.execute(requestorder)
        
        total_paid = response_data.result.purchase_units[0].amount.value
        Ordered_Item    = data['Ordered_Items']
        pickup_point    = data['Customer_Pickup_point']
        
        
        if serializers.is_valid(raise_exception=True):
                        
            order = Order.objects.create(user_id=data['user_id'], payment_id = response_data.result.id, amount_paid=total_paid,
                                Payment_method='Paypal',delivery_method=data['delivery_method'], payment_status = True )
            
            order_id = order.pk
            
            for item in Ordered_Item:
                
                Ordered_Items.objects.create(order_id = order_id, product = data['product'], quantity = data['quantity'], price = data['price'])
            
            for pickup in pickup_point:
                
                Customer_Pickup_point.objects.create(order_id = order_id, user_id=data['user_id'],Station_id = data['Station_id'],
                                                    first_name=data['user_id'], last_name=data['last_name'], phone_number=data['phone_number'],
                                                    Delivery_address=data['Delivery_address'], County=data['County'], City=data['City'] )
                
            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )
    
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    