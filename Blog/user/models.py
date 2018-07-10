from django.db import models

# Create your models here.

class User(models.Model):
    SEX = (
        ('M',"男"),
        ('F',"女"),
        ('U',"保密"),
    )
    nickname = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    icon = models.ImageField()
    age = models. IntegerField()
    sex = models. CharField(max_length=8, choices=SEX)