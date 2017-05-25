# Serializers define the API representation.
from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'bio', 'is_staff')
