import json
import os
from json import loads

from rest_framework.response import Response
from rest_framework.views import APIView


class Song(APIView):

    def __init__(self):
        # Build paths inside the project like this: BASE_DIR / 'subdir'.
        BASE_DIR = os.path.dirname('/code/')

        # Read songs.json file
        with open(BASE_DIR + '/songs.json') as json_file:
            songs_file = json.load(json_file)

        self.songs = songs_file['feed']['results']

    # def get(self, request, song_id):
    #     # Get a song by id
    #     output = filter(lambda song: song['id'] == str(song_id), self.songs)
    #
    #     return Response(output)

    def get(self, request, song_name):
        # Get a song by name
        output = next((son for son in self.songs if son['name'] == song_name), None)
        return Response(output)

    def delete(self, request, song_id):
        # Build paths inside the project like this: BASE_DIR / 'subdir'.
        BASE_DIR = os.path.dirname('/code/')

        # Read songs.json file
        data = loads(request.body.decode('utf-8'))
        with open(BASE_DIR + '/songs.json', 'r+') as file:
            songs_file = json.load(file)
            songs = songs_file['feed']['results']

        for i in range(len(songs)):
            if songs[i]['id'] == str(song_id):
                songs.pop(i)
                break
        # Add a song in a json file
        output = data
        return Response(output)
