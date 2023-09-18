from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class TokenAPIView(APIView):
    def get(self, request: Request):
        token = request.query_params.get('token')

        if token is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            user = Token.objects.get(key=token).user
        except Exception:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return Response(data={'user_id': user.id})
