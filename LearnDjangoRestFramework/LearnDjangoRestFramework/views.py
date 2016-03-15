from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

class APIRoot(generics.GenericAPIView):
	queryset = User.objects.all()
	def get(self,request,format=None):
		return Response({
			'users': reverse('user-list', request=request, format=format),
			'snippets': reverse('snippet-list', request=request, format=format)
		})