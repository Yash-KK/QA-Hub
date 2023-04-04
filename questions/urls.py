from django.urls import path

from .views import (
    QuestionListAPI
)
urlpatterns = [
    path('questions/', QuestionListAPI.as_view(),name='question-list')
]
