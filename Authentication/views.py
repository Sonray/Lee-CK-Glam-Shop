from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions

# Create your views here.

@permission_classes((permissions.AllowAny,))
class RegisterUser(APIView):

    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        
        user = request.data
        serializers = self.serializer_class(data=user)

        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


