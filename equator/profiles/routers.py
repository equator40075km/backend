from rest_framework import routers
from .views import ProfileViewSet


profile_router = routers.DefaultRouter()
profile_router.register(r'', ProfileViewSet)
