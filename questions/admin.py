from django.contrib import admin

#MODEL
from .models import (
    Question,
    Answer
)
# Register your models here.

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['body', 'author', 'all_voters']
admin.site.register(Question)
admin.site.register(Answer, AnswerAdmin)

