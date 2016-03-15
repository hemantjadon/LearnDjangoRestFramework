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


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.

class SnippetList(APIView):
	permission_classes = [IsAdminUser]
	queryset = Snippet.objects.all()
	
	def get(self,request,format=None):
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True,context={'request': request})
		return Response(serializer.data,status = status.HTTP_200_OK)
		
	def post(self,request,format=None):
		serializer = SnippetSerializer(data=request.data,context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
	permission_classes = [IsAdminUser]
	queryset = Snippet.objects.all()
	
	def get_object(self,pk):
		try:
			return Snippet.objects.get(pk=pk)
		except Snippet.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		
	def get(self,request,pk,format=None):
		snippet = self.get_object(pk)
		serializer = SnippetSerializer(snippet,context={'request': request})
		return Response(serializer.data,status=status.HTTP_200_OK)
	
	def put(self,request,pk,format=None):
		snippet = self.get_object(pk)
		serializer = SnippetSerializer(snippet,data=request.data,context={'request': request})
		if serializer.is_valid():
			return Response(serializer.data,status=status.HTTP_200_OK)
		else:
			return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self,request,pk,format=None):
		snippet = self.get_object(pk)
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		
class SnippetViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminUser]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer