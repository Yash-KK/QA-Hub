from rest_framework import serializers

#MODEL
from .models import (
    Question,
    Answer
)

class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()   
    answer_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = Question
        exclude = ['id','modified_at']

    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')    
    
    def get_answer_count(self, obj):
        return obj.answers.count()
    
    def get_user_has_answered(self,obj):
        authenticated_user = self.context.get('request').user
        return obj.answers.filter(author=authenticated_user).exists()

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    likes_count = serializers.SerializerMethodField()
    question_slug = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        exclude = ['modified_at', 'question', 'voters']

    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')    
    
    def get_likes_count(self, obj):
        return obj.voters.count()
    
    def get_question_slug(self, obj):
        return obj.question.slug

    def get_user_has_liked(self, obj):
        authenticated_user = self.context.get('request').user
        return obj.voters.filter(pk=authenticated_user.pk).exists()
    