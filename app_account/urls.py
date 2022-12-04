from django.urls import path

from app_account.views import Login, Signup, ForgetPassword, UpdatePassword

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('sign-up', Signup.as_view(), name='sign_up'),
    path('update-password', UpdatePassword.as_view(), name='sign_up'),
    path('forget-password', ForgetPassword.as_view(), name='sign_up'),
]
