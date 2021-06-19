from django.contrib.auth.models import User
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    PrimaryKeyRelatedField,
    )

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']