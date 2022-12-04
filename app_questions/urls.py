from django.urls import path

from app_questions.views import GetListQuestion

urlpatterns = [
    path('get-set-question', GetListQuestion.as_view())
]
