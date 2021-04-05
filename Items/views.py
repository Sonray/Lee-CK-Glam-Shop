from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Reviews, Product_details
from .serializers import ProductSerializer, ReviewSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions, generics, status

# Create your views here.


@permission_classes((permissions.AllowAny,))
class Display_all_products(APIView):
    
    def get(self, request, format=None):
        all_post = Product_details.objects.all()
        serializers = ProductSerializer(all_post, many=True)
        return Response(serializers.data)
        
        

@permission_classes((permissions.AllowAny,))
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



@permission_classes((permissions.AllowAny,))
class Make_a_review(APIView):    

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
class Display_all_Reviews(APIView):
    pass

