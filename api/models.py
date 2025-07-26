from django.db import models

STATUS_CHOICES = (
    ('watching', 'Watching'),
    ('completed', 'Completed'),
    ('wishlist', 'Wishlist'),
)

class MovieTV(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    is_tv_show = models.BooleanField(default=False)
    total_episodes = models.IntegerField(null=True, blank=True)
    episodes_watched = models.IntegerField(default=0)

    def __str__(self):
        return self.title

from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    movie = models.ForeignKey(MovieTV, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie.title} - {self.rating}/5'



# Create your models here.
