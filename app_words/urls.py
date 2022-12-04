from django.urls import path
from app_words.views import GetRandomWord, GetWordDefinition


urlpatterns = [
    path('random-word', GetRandomWord.as_view()),
    path('word-definition', GetWordDefinition.as_view()),
]
