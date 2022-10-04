from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from authapp.models import User
from django.contrib.auth.hashers import make_password


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserModelSerializer, self).create(validated_data)
