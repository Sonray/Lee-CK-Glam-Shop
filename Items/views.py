from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Reviews, Product_details,Order, Order_Made_by_Mpesa
from .serializers import ProductSerializer, ReviewSerializer, OrderSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions, generics, status, filters
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
import requests
from .payments import Lipa_na_mpesa

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
class  Mpesa_payment(APIView):
    
    serializer_class = ReviewSerializer

    def post(self, request, format=None):
        
        review = request.data
        serializers = self.serializer_class(data=review)

        if serializers.is_valid(raise_exception=True):

            serializers.save()
            
            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@permission_classes((permissions.AllowAny,)) 
class  Order_Product(APIView):
    
    serializer_class = OrderSerializer

    def post(self, request, format=None):
        
        review = request.data
        serializers = self.serializer_class(data=review)

        if serializers.is_valid(raise_exception=True):
            
            phone_number = str( review['order_phone_number'])
            amount_1 = str(review['price'])
            
            mpesa_dict = Lipa_na_mpesa( phone_number, amount_1)
            
            MerchantRequestID = mpesa_dict['MerchantRequestID']
            CheckoutRequestID = mpesa_dict['CheckoutRequestID']
            
            Order_item = Product_details.objects.filter(pk=review['Order_items']) 
            
            # instance = Order.objects.create(organization=org)            
            instance = serializers.create(request, MerchantRequestID, CheckoutRequestID)
            
            instance.Order_items.set(Order_item)
            instance.save()
             
            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    