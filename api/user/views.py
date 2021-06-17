from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets

# Create your views here.
class UserAPI(viewsets.ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer