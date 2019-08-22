from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    organiser=models.CharField(max_length=15,default="")
    name_quiz=models.CharField(max_length=15,unique=True)
    number_quiz=models.IntegerField(default=0)

class Questions(models.Model):
    relation=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question=models.CharField(max_length=100000,default="")
    option1=models.CharField(max_length=10000,default="")
    option2=models.CharField(max_length=10000,default="")
    option3=models.CharField(max_length=10000,default="")
    correct=models.CharField(max_length=10000,default="")


class User_Info(models.Model):
    relation=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=15,default="")
    score=models.IntegerField(default=0)

class Test_Score(models.Model):
    relation=models.ForeignKey(User,on_delete=models.CASCADE)
    score_test=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    score=models.IntegerField(default=0)

class Feedback(models.Model):
    name=models.CharField(max_length=15,default="")
    email=models.CharField(max_length=15,default="")
    subject=models.CharField(max_length=15,default="")
    message=models.CharField(max_length=15,default="")

