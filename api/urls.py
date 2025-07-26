from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieTVViewSet, ReviewViewSet,recommend_movies

router = DefaultRouter()
router.register(r'movies', MovieTVViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('recommendations/<int:user_id>/', recommend_movies, name='recommend-movies'),
]


