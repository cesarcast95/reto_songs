import json
import os
from json import loads

from rest_framework.response import Response
from rest_framework.views import APIView


class Songs(APIView):

    def __init__(self):
        # Build paths inside the project like this: BASE_DIR / 'subdir'.
        BASE_DIR = os.path.dirname('/code/')

        # Read songs.json file
        with open(BASE_DIR + '/songs.json') as json_file:
            songs_file = json.load(json_file)
        self.songs = songs_file['feed']['results']

    def get(self, request):
        # Get 50 top songs
        output = self.songs[:50]
        print(output)
        return Response(output)

    def post(self, request, **kwargs):

        # Build paths inside the project like this: BASE_DIR / 'subdir'.
        BASE_DIR = os.path.dirname('/code/')

        # Read songs.json file
        data = loads(request.body.decode('utf-8'))
        with open(BASE_DIR + '/songs.json', 'r+') as file:
            songs_file = json.load(file)
            songs_file['feed']['results'].append(data)
            file.seek(0)
            json.dump(songs_file, file, indent=4)
        # Add a song in a json file
        output = data
        return Response(output)
