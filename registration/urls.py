from django.urls import path
from .views import *

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('loginname/', UserLoginUsername.as_view()),
    path('loginemail/', UserLoginEmail.as_view()),
]