from django.contrib import admin

#MODEL
from .models import (
    Question,
    Answer
)
# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
