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

class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
	permission_classes = [IsAdminUser]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	
	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)
		
	def post(self,request,format=None):
		return self.create(request,*args,**kwargs)

class SnippetDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
	permission_classes = [IsAdminUser]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
		
	def get(self,request,*args,**kwargs):
		return self.retrive(request,*args,**kwargs)
	
	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)
	
	def delete(self,request,pk,format=None):
		return self.destroy(request,*args,**kwargs)
		
class SnippetViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminUser]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer