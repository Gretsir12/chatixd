from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserCreateView.as_view()),
    path('messages/', MessageListCreateView.as_view()),
    path('contacts/', UserContactsView.as_view()),
]