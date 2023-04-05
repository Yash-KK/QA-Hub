from django.urls import path

from .views import (
    QuestionListAPI,
    QuestionDetailAPI,

    AnswerCreateAPI,
    AnswerListAPI,
    AnswerDetailAPI,

    AnswerLikeAPI
)
urlpatterns = [
    path('questions/', QuestionListAPI.as_view(),name='question-list'),
    path('questions/<slug:slug>/', QuestionDetailAPI.as_view(), name='question-detail'),

    path('questions/<slug:slug>/answer-create/', AnswerCreateAPI.as_view(), name='answer-create'),
    path('questions/<slug:slug>/answers/', AnswerListAPI.as_view(), name='answer-list'),

    path('answers/<int:pk>/',AnswerDetailAPI.as_view(), name='answer-detail'),
    path('answers/<int:pk>/like/',AnswerLikeAPI.as_view(), name='answer-like')

]
