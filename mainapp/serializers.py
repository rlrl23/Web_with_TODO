from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from mainapp.models import Project, Todo
from authapp.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'
