from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import status
from .models import Task

# Create your views here.
class TaskAPI(viewsets.ModelViewSet): 
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(project_id=self.kwargs.get('project_id'))