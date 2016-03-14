from django.shortcuts import render
from rest_framework import viewsets
from quickstart.serializers import *
from rest_framework import routers

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

router = routers.DefaultRouter()
router.register(r'^users', UserViewSet)
router.register(r'^groups', GroupViewSet)
