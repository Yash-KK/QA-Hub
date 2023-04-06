from django.shortcuts import render

#REST_FRAMEWORK
from rest_framework import (
    generics
)
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,

    HTTP_400_BAD_REQUEST
)
from .paginations import (
    NoCountPagination
)
from rest_framework.permissions import (
    IsAuthenticated
)
from .permissions import (
    IsAuthorOrReadOnly
)

#SERIALIZER
from .serializer import (
    QuestionSerializer,
    AnswerSerializer
)

#MODEL
from .models import (
    Question,
    Answer
)
# Create your views here.

class QuestionListAPI(generics.ListCreateAPIView):
    pagination_class = NoCountPagination
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def perform_create(self, serializer):
        authenticated_user = self.request.user
        serializer.save(author=authenticated_user)

class QuestionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    lookup_field = 'slug'

class AnswerCreateAPI(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def perform_create(self, serializer):
        slug = self.kwargs['slug']
        authenticated_user = self.request.user
        question_instance = Question.objects.get(slug=slug)

        if Answer.objects.filter(author=authenticated_user, question=question_instance).exists():
            raise ValidationError("User has already answered this question!")
        
        serializer.save(author=authenticated_user, question=question_instance)

class AnswerListAPI(generics.ListAPIView):
    pagination_class = NoCountPagination
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get_queryset(self):
        question_slug = self.kwargs['slug']
        return Answer.objects.filter(question__slug=question_slug)


class AnswerDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = AnswerSerializer
    queryset = Answer.objects.filter()


class AnswerLikeAPI(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerSerializer

    def post(self, request, pk):
        answer = Answer.objects.get(pk=pk)
        answer.voters.add(request.user)
        answer.save()        
        serializer = self.serializer_class(answer,context={'request': request})
        return Response(serializer.data, status=HTTP_200_OK)
    
    def delete(self, request, pk):
        answer = Answer.objects.get(pk=pk)
        answer.voters.remove(request.user)
        answer.save()

        serializer = self.serializer_class(answer, context={'request': request})
        return Response(serializer.data, status=HTTP_200_OK)
    
    