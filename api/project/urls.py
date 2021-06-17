# from django.urls import path
from .views import ProjectAPI
from ..task.views import TaskAPI

# urlpatterns = [
#     path('',ProjectAPI.as_view(), name='project')
# ]

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', ProjectAPI, basename='project')
router.register(r'(?P<project_id>\d+)/tasks', TaskAPI, basename='Tasks')
#...

urlpatterns = router.urls