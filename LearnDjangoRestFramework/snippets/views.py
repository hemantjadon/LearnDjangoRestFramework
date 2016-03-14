from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True,context={'request': request})
        return Response(serializer.data,status = status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAdminUser])
def snippet_detail(request,pk):
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'GET':
		serializer = SnippetSerializer(snippet,context={'request': request})
		return Response(serializer.data,status=status.HTTP_200_OK)
	
	elif request.method == 'PUT':
		serializer = SnippetSerializer(snippet,data=request.data,context={'request': request})
		if serializer.is_valid():
			return Response(serializer.data,status=status.HTTP_200_OK)
		else:
			return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		
class SnippetViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminUser]
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer