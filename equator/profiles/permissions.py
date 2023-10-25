from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist


class IsProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        try:
            user_id: int = Token.objects.get(key=request.auth).user.id
            return user_id == obj.id
        except ObjectDoesNotExist:
            return False
