from django.shortcuts import render

#REST_FRAMEWORK
from rest_framework import (
    generics,
    status
)

#SERIALIZER
from .serializer import (
    QuestionSerializer
)

#MODEL
from .models import (
    Question
)
# Create your views here.

class QuestionListAPI(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def perform_create(self, serializer):
        authenticated_user = self.request.user
        serializer.save(author=authenticated_user)
