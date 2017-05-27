from rest_framework import viewsets

from .serializers import UserSerializer
from ..models import User

class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
