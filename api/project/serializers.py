from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    PrimaryKeyRelatedField,
    )

from api.task.serializers import TaskSerializer

from .models import Project   

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
