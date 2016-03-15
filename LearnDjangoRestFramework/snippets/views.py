from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework import mixins
from rest_framework import generics
from rest_framework import renderers

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.permissions import IsOwnerOrReadOnly

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [IsOwnerOrReadOnly]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

class SnippetHighlight(generics.GenericAPIView):
	queryset = Snippet.objects.all()
	renderer_classes = (renderers.StaticHTMLRenderer,)
	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

		
class SnippetViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminUser]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer