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