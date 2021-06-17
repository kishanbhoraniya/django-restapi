from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('user/',include('api.user.urls')),
    path('project/',include('api.project.urls')),
]