from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProjectSerializer
from rest_framework import status
from .models import Project

# Create your views here.
class ProjectAPI(viewsets.ModelViewSet):    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer