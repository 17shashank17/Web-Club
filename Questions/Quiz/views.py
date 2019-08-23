from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import Questions,Quiz,User_Info,Test_Score,Feedback
import json
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

def home(request):
    #return HttpResponse("<h1>Welcome</h1>")
    return render(request,'Quiz/home.html')

def quiz_all(request):
    try:
        username=request.session['username']
        print(username)
        user=User.objects.get(username=username)
        q=Quiz.objects.all()
        attempted_quiz=Test_Score.objects.filter(relation=user)
        quiz_name=[]
        for i in attempted_quiz:
            quiz_name.append(i.score_test)
        print(quiz_name)
        return render(request,'Quiz/quizall.html',{'q':q,'quiz_name':quiz_name})
    except:
        return HttpResponseRedirect('/quiz/login/')
     

def questions(request,id):
    if request.method=="POST":
        score=request.POST.get('score')
        username=request.session['username']
        user=User.objects.get(username=username)
        user_info=User_Info.objects.get(relation=user)
        user_info.score+=int(score)
        user_info.save()
        test_score=Test_Score()
        test_score.relation=user
        test_score.score_test=Quiz.objects.get(name_quiz=request.session['quiz_name'])
        test_score.score=int(score)
        test_score.attempted=True
        test_score.save()
        return HttpResponseRedirect('/quiz/profile/')
        
    else:
        try:
            username=request.session['username']
            quiz=Quiz.objects.get(id=id)
            quiz_name=quiz.name_quiz
            request.session['quiz_name']=quiz_name
            #question_set=Questions.objects.filter(relation=quiz).item_list('question','option1','option2','option3','correct')
            #context={'question_set':question_set}
            #data = serializers.serialize('json', context)
            #data=json.dumps(list(context),cls=DjangoJSONEncoder)
            question_set=Questions.objects.filter(relation=quiz)
            return render(request,"Quiz/take_quiz.html",{'question_set':question_set,})
        except:
            return HttpResponseRedirect('/quiz/login/')

def login_user(request):
    if request.method=="POST":
        username=request.POST.get('username')
        request.session['username']=username
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return render(request,'Quiz/profile.html',{'username':username})
    else:
        return render(request,'Quiz/login.html')

def profile(request):
    username=request.session['username']
    return render(request,'Quiz/profile.html',{'username':username})

def performance(request):
    username=request.session['username']
    user=User.objects.get(username=username)
    user_info=User_Info.objects.get(relation=user)
    test_attempted=Test_Score.objects.filter(relation=user)
    context={
        'user_info':user_info,
        'test_attempted':test_attempted,
    }
    return render(request,'Quiz/performance.html',context)

def leaderboard(request):
    user_info=User_Info.objects.all()

    return render(request,'Quiz/leaderboard.html',{'user_info':user_info,})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/quiz')

def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        request.session['username']=username
        password=request.POST.get("password")
        name=request.POST.get("name")
        try:
            user=User.objects.get(username=username)
            #return
        except:
            user=User()
            user.username=username
            user.set_password(str(password))
            user.save()
            user_info=User_Info()
            user_info.relation=user
            user_info.name=name
            user_info.username=username
            user_info.save()
        return render(request,'Quiz/profile.html',{'username':username})
    else:
        return render(request,'Quiz/signup.html')

def create_quiz(request):
    try:
        username=request.session['username']
        if request.method=="POST":
            name=request.POST.get('contest_name')
            try:
                quiz=Quiz.objects.get(name_quiz=name)
                quest=Questions()
                quest.relation=quiz
                quest.question=request.POST.get('question')
                quest.option1=request.POST.get('option1')
                quest.option2=request.POST.get('option2')
                quest.option3=request.POST.get('option3')
                quest.correct=request.POST.get('correct')
                quest.save()
                return HttpResponseRedirect('/quiz/create_quiz')
            except:    
                quiz=Quiz()
                quiz.name_quiz=name
                quiz.organiser=username
                quiz.save()
                quest=Questions()
                quest.relation=quiz
                quest.question=request.POST.get('question')
                quest.option1=request.POST.get('option1')
                quest.option2=request.POST.get('option2')
                quest.option3=request.POST.get('option3')
                quest.save()
                return HttpResponseRedirect('/quiz/create_quiz')

        else:

            return render(request,'Quiz/create_quiz.html')
    except:
        return HttpResponseRedirect('/quiz/login')


def feedback(request):
    if request.method=="POST":
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        subject=request.POST.get('Subject')
        message=request.POST.get('Message')

        print(name,message)

        msg=Feedback()
        msg.name=name
        msg.email=email
        msg.subject=subject
        msg.message=message
        msg.save()

        return render(request,'Vote/home.html')

    else:
        return render(request,'Vote/home.html')