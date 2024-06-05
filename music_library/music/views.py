from rest_framework import generics
from .models import Artist, Song
from .serializers import ArtistSerializer, SongSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ArtistListCreate(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongListCreate(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

@api_view(['GET'])
def artist_songs(request, artist_id):
    try:
        artist = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        return Response(status=404)

    songs = artist.songs.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)
