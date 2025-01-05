from __future__ import annotations
from django.db import models
# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)


class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="players", null=True, blank=True
    )
    age = models.IntegerField()


class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
