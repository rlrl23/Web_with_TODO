from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from authapp.models import User
from authapp.serializers import UserModelSerializer


class UserModelViewSet(GenericViewSet,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
# Create your views here.
