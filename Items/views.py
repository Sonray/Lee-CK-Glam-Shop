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
    pass


@permission_classes((permissions.AllowAny,))
class Make_a_review(APIView):
    pass


@permission_classes((permissions.AllowAny,))
class Display_all_Reviews(APIView):
    pass

