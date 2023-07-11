from django.shortcuts import render
from requests import request
from rest_framework.viewsets import ModelViewSet

from authapp.models import User
from authapp.serializers import UserModelSerializer, UserModelSerializerBase


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserModelSerializerBase
        return UserModelSerializer
