from django.urls import path, include
from .routers import profile_router
from .views import TokenAPIView, ProfileFavoritesAPIView


urlpatterns = [
    path('profiles/', include(profile_router.urls)),
    path('token/', TokenAPIView.as_view()),
    path('profiles/<int:profile_id>/favorites/', ProfileFavoritesAPIView.as_view()),
    path('profiles/<int:profile_id>/favorites/<int:article_id>/', ProfileFavoritesAPIView.as_view())
]
