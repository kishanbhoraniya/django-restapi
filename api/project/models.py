from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now = True, null=True, blank=True)
    avatar = models.ImageField(upload_to = "images/upload/", blank=True)
    is_active = models.BooleanField(default=True)

        