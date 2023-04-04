from django.db import models
from QAhub.settings import AUTH_USER_MODEL

from django.utils.text import slugify
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

class Question(TimeStamp):
    content = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, unique=True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='questions')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.content) + '-' + get_random_string(4)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.content}"
    
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Question's"

class Answer(TimeStamp):
    body = models.CharField(max_length=140)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answers')
    voters = models.ManyToManyField(AUTH_USER_MODEL, related_name='likes')

    def __str__(self):
        return f"{self.body}: {self.author.username}"
    
    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = "Answer's"

