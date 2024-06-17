from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.conf import settings
from prompt_generator import prompt_generator
from song_generator import song_generator

class SongGeneratorView(APIView):
    def post(self, request):
        spotify_track_id = request.data.get('spotify_track_id')
        if spotify_track_id == None:
            raise serializers.ValidationError({'spotify_track_id': 'This field is required.'})

        prompt = prompt_generator.generate_prompt_from_spotify_track_id(spotify_track_id)

        song_file_path = song_generator.generate_song(prompt)

        return Response({
            'prompt': prompt,
            'generated_song': song_file_path
        })
