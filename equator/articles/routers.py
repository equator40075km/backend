from rest_framework import routers
from .views import ArticleViewSet


article_router = routers.DefaultRouter()
article_router.register(r'', ArticleViewSet)
