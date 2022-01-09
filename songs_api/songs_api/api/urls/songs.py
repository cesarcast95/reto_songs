from django.urls import path
from api.src.songs.views.song import Song
from api.src.songs.views.songs import Songs

urlpatterns = [
    path('songs/<int:song_id>', Song.as_view()),
    path('songs/<str:song_name>/', Song.as_view()),
    path('songs', Songs.as_view())
]
