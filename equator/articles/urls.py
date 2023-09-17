from django.urls import path, include
from .routers import article_router


urlpatterns = [
    path('articles/', include(article_router.urls))
]
