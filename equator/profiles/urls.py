from django.urls import path, include
from .routers import profile_router
from .views import TokenAPIView


urlpatterns = [
    path('profiles/', include(profile_router.urls)),
    path('token/', TokenAPIView.as_view())
]
