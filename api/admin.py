from django.contrib import admin
from .models import MovieTV, Review

@admin.register(MovieTV)
class MovieTVAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'director', 'genre', 'platform', 'status', 'is_tv_show')
    list_filter = ('genre', 'platform', 'status', 'is_tv_show')
    search_fields = ('title', 'director')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('movie__title', 'review_text')


# Register your models here.


# Register your models here.
