from django.urls import path
from app_api.views import Test, GetTheory, ReturnNoneImage

urlpatterns = [
    path('', Test.as_view()),
    path('get-theory', GetTheory.as_view(), name='get-theory'),
    path('assets/images/arrow_right.png', ReturnNoneImage.as_view()),
    path('assets/images/arrow_down.png', ReturnNoneImage.as_view()),
]
