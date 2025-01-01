from django.db import models

# Create your models here.


class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
