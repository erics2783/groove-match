from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.conf import settings
from external_apis.spotify_api import SpotifyApi


class SongSearchView(APIView):
    def post(self, request):
        query = request.data.get('query')
        if query == None:
            raise serializers.ValidationError({'query': 'This field is required.'})

        spotify = SpotifyApi(settings.SPOTIFY['URL'], settings.SPOTIFY['CLIENT_ID'], settings.SPOTIFY['CLIENT_SECRET'])
        search_result = spotify.search(query)
        return Response(list(map(lambda track: {
            'id': track['id'],
            'name': track['name'],
            'artists': ', '.join(list(map(lambda artist: artist['name'], track['artists']))),
            'album': track['album']['name'],
            'image': track['album']['images'][0]['url']
        }, search_result['tracks']['items'])))

