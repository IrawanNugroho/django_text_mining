from django.urls import path
from main.views import TextPreprocessing

urlpatterns = [
    path('preprocessing/', TextPreprocessing.as_view()),
]