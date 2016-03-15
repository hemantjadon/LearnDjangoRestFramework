from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	
	def has_object_permission(self,request,view,obj):
		if request.method in ['GET','HEAD','OPTIONS']:
			return True
		
		elif request.method in ['PUT','PATCH','DELETE']:
			if request.user == obj.owner:
				return True
			else:
				return False
		else:
			return False
				