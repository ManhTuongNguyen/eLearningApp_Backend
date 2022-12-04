import json
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .models import MostCommonWord
from random import randint
import urllib3

urllib3.disable_warnings()


class GetRandomWord(APIView):
    def get(self, request):
        max_length = MostCommonWord.objects.count()
        random_index = randint(1, max_length)
        random_word = MostCommonWord.objects.get(pk=random_index).word
        random_word = random_word.replace('\n', '')
        api_dictionary = f'https://api.dictionaryapi.dev/api/v2/entries/en/{random_word}'
        definition = requests.get(api_dictionary, verify=False)
        response = json.loads(definition.content.decode())
        return Response(response)


class GetWordDefinition(APIView):
    def get(self, request):
        word = request.GET.get('word')
        api_dictionary = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
        definition = requests.get(api_dictionary, verify=False)
        response = json.loads(definition.content.decode())
        # Handle data here

        return Response(response)













