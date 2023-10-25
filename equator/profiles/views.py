from rest_framework import status, mixins, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import Profile
from .serializers import ProfileSerializer
from .permissions import IsProfileOwner


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsProfileOwner]


class TokenAPIView(APIView):
    def get(self, request: Request):
        if request.auth:
            return Response(data={'user_id': request.auth.user.id})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
