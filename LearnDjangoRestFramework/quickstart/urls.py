from django.conf.urls import url,include
from quickstart.views import UserViewSet,GroupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('groups',GroupViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
]
