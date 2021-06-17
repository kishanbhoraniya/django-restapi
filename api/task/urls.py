# from django.urls import path
from .views import TaskAPI

# urlpatterns = [
#     path('',ProjectAPI.as_view(), name='project')
# ]

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', TaskAPI, basename='task')
#...

urlpatterns = router.urls