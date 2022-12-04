from django.urls import path
from app_score.views import GetListSetQuestion, UpdateScore

urlpatterns = [
    path('get-list-set-question', GetListSetQuestion.as_view()),
    path('update-score', UpdateScore.as_view())
]
