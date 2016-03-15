from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import mixins
from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
	permission_classes = [IsAdminUser]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAdminUser]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
		
class SnippetViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminUser]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer