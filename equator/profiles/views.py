from rest_framework import status, mixins, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import Profile
from .serializers import ProfileSerializer
from articles.serializers import Article
from django.forms.models import model_to_dict
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


class ProfileFavoritesAPIView(APIView):
    def get(self, request: Request, *args, **kwargs):
        if not request.auth:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        profile_id = kwargs.get('profile_id', None)
        if not profile_id:
            return Response({'error': 'profile_id is None'})

        favorites = Profile.objects.get(id=profile_id).favorites.all()
        result = []
        for article in favorites:
            result.append(model_to_dict(article, exclude=['text']))

        return Response(result)

    def put(self, request, *args, **kwargs):
        return self.__change_favorites(True, request, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.__change_favorites(False, request, kwargs)

    def __change_favorites(self, add: bool, request, kwargs):
        def m_auth(_request: Request) -> bool:
            if _request.auth:
                return True

            if not _request.data or \
                    'headers' not in _request.data or \
                    'Authorization' not in _request.data.get('headers', {}):
                return False

            _token = _request.data['headers']['Authorization'].replace('Token ', '')
            return Token.objects.filter(key=_token).first() is not None

        if not m_auth(request):
            return Response(
                {'error': 'request.auth is None'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        profile_id = kwargs.get('profile_id', None)
        article_id = kwargs.get('article_id', None)
        if not profile_id or not article_id:
            return Response(
                {'error': 'profile_id or article_id is None'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        article = Article.objects.filter(id=article_id).first()
        profile = Profile.objects.filter(id=profile_id).first()
        if not article or not profile:
            return Response(
                {'error': 'profile or article is None'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        if add:
            profile.favorites.add(article)
            article.rating += 1
        else:
            profile.favorites.remove(article)
            article.rating -= 1

        article.save()

        return Response(
            model_to_dict(article),
            status=status.HTTP_200_OK
        )
