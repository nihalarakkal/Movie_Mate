from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import MovieTV, Review
from .serializers import MovieTVSerializer, ReviewSerializer

# MovieTV ViewSet
class MovieTVViewSet(viewsets.ModelViewSet):
    queryset = MovieTV.objects.all().order_by('-id')
    serializer_class = MovieTVSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-id')
    serializer_class = ReviewSerializer

# Recommendation API View (based on authenticated user)

@api_view(['GET'])
def recommend_movies(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    # Get top-rated genres by user and remove duplicates
    top_reviews = Review.objects.filter(user=user, rating__gte=4)
    top_genres = list(set(top_reviews.values_list('movie__genre', flat=True)))

    recommended = MovieTV.objects.filter(
        genre__in=top_genres
    ).exclude(reviews__user=user).distinct()

    seen_ids = set()
    data = []

    for m in recommended:
        if m.id not in seen_ids:
            seen_ids.add(m.id)
            data.append({
                "id": m.id,
                "title": m.title,
                "genre": m.genre,
                "platform": m.platform,
                "status": m.status
            })

    return Response(data)

# Create your views here.
