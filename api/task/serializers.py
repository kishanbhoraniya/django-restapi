from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    PrimaryKeyRelatedField,
    ManyRelatedField
    )

from .models import Task   

class SubTaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title']


class TaskSerializer(ModelSerializer):
    sub_tasks = SubTaskSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__' 
