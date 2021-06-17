from django.urls import path
from .views import UserAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', UserAPI, basename='user')
#...

urlpatterns = router.urls