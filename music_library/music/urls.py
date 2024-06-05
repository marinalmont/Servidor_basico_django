from django.urls import path
from .views import (
    ArtistListCreate, ArtistRetrieveUpdateDestroy,
    SongListCreate, SongRetrieveUpdateDestroy,
    artist_songs
)

urlpatterns = [
    path('artists/', ArtistListCreate.as_view(), name='artist_list_create'),
    path('artists/<int:pk>/', ArtistRetrieveUpdateDestroy.as_view(), name='artist_retrieve_update_destroy'),
    path('songs/', SongListCreate.as_view(), name='song_list_create'),
    path('songs/<int:pk>/', SongRetrieveUpdateDestroy.as_view(), name='song_retrieve_update_destroy'),
    path('artists/<int:artist_id>/songs/', artist_songs, name='artist_songs'),
]
