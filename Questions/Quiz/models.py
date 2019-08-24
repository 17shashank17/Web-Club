from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    #relation=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    organiser=models.CharField(max_length=200,default="")
    name_quiz=models.CharField(max_length=200,unique=True)
    number_quiz=models.IntegerField(default=0)
    attempt=models.IntegerField(default=0,blank=True,null=True)

class Questions(models.Model):
    relation=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question=models.CharField(max_length=100000,default="")
    option1=models.CharField(max_length=10000,default="")
    option2=models.CharField(max_length=10000,default="")
    option3=models.CharField(max_length=10000,default="")
    correct=models.CharField(max_length=10000,default="")
    option1_per=models.IntegerField(default=0,blank=True,null=True)
    option2_per=models.IntegerField(default=0,blank=True,null=True)
    option3_per=models.IntegerField(default=0,blank=True,null=True)



class User_Info(models.Model):
    relation=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=200,default="")
    name=models.CharField(max_length=15,default="")
    score=models.IntegerField(default=0)


class Test_Score(models.Model):
    relation=models.ForeignKey(User,on_delete=models.CASCADE)
    score_test=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    attempted=models.BooleanField(default=False)
    score=models.IntegerField(default=0)

class Feedback(models.Model):
    name=models.CharField(max_length=15,default="")
    email=models.CharField(max_length=15,default="")
    subject=models.CharField(max_length=15,default="")
    message=models.CharField(max_length=15,default="")

