from rest_framework import routers
from quickstart.views import UserViewSet,GroupViewSet
from snippets.views import SnippetViewSet 

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('groups',GroupViewSet)
router.register('snippets',SnippetViewSet)