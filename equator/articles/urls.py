from django.urls import path, include

from . import routers


urlpatterns = [
    path('articles/', include(routers.article_router.urls))
]
