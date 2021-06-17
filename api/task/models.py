from django.db import models
from django.contrib.auth.models import User
from ..project.models import Project


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=200)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    created_at = models.DateTimeField(auto_now = True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name= 'tasks', null=True)    
    parent_id = models.ForeignKey("self", on_delete=models.CASCADE, related_name= 'sub_tasks', null=True)
