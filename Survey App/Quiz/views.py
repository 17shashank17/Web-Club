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

'''def results(request):
    
    questions=Questions.objects.all()
    try:
        username=request.session['username']
        print(username)
        return render(request,'Quiz/results.html',{'questions':questions,'username':True,})
    except:
        return render(request,'Quiz/results.html',{'questions':questions,'username':False,})'''

def results(request):
    if request.method=="POST":
        survey_name=request.POST.get('survey_results')
        quiz=Quiz.objects.get(name_quiz=survey_name)
        question_set=Questions.objects.filter(relation=quiz)
        try:
            username=request.session['username']
            return render(request,'Quiz/survey_results.html',{'question_set':question_set,'username':True})
        except:
            return render(request,'Quiz/survey_results.html',{'question_set':question_set,'username':False})
    else:
        survey=Quiz.objects.all()
        try:
            username=request.session['username']
            return render(request,'Quiz/results.html',{'survey':survey,'username':True,})
        except:
            return render(request,'Quiz/results.html',{'survey':survey,'username':False,})
    

def questions(request,id):
    if request.method=="POST":
        score=request.POST.get('score')
        username=request.session['username']
        quiz_name=request.session['quiz_name']
        ans=request.POST.get('ans')
        ans=ans.split(':')
        quiz=Quiz.objects.get(name_quiz=quiz_name)
        quiz.attempt+=1
        quiz.save()
        div=quiz.attempt
        questions_set=Questions.objects.filter(relation=quiz)
        for i in questions_set:
            for j in range(len(ans)):
                if i.option1==ans[j].strip():
                    i.option1_per+=1
                    break
                elif i.option2==ans[j].strip():
                    i.option2_per+=1
                    break
                elif i.option3_per==ans[j].strip():
                    i.option3+=1
                    break
            i.option1_percentage=(i.option1_per/div)*100
            i.option2_percentage=(i.option2_per/div)*100
            i.option3_percentage=(i.option3_per/div)*100
            i.save()
        user=User.objects.get(username=username)
        user_info=User_Info.objects.get(relation=user)
        user_info.save()
        test_score=Test_Score()
        test_score.relation=user
        test_score.score_test=Quiz.objects.get(name_quiz=request.session['quiz_name'])
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
    return render(request,'Quiz/profile.html',{'username':username,})

def your_quiz(request):
    if request.method=="POST":
        try:
            id_delete=request.POST.get("id-value-delete")
            quiz=Quiz.objects.get(id=id_delete)
            quiz.delete()
            return HttpResponseRedirect('/quiz/your_quiz')
        except:
            id_modify=request.POST.get("id-value-modify")
            #quiz=Quiz.objects.get(id=id_modify)
            request.session['id']=id_modify
            #questions=Questions.objects.filter(relation=quiz)
            #return render(request,'Quiz/modify.html',{'questions':questions})
            return HttpResponseRedirect('/quiz/modify')
    else:
        username=request.session['username']
        quiz=Quiz.objects.filter(organiser=username)
        return render(request,'Quiz/your_quiz.html',{'quiz':quiz,})

def modify_quiz(request):
    if request.method=="POST":
        
        id_delete=request.POST.get("id-delete-question")
        print(id_delete)
        if id_delete is not None:
            quest=Questions.objects.get(id=id_delete)
            quest.delete()
            return HttpResponseRedirect('/quiz/modify')
        else:
            contest_name=request.POST.get('contest_name')
            quiz=Quiz.objects.get(name_quiz=contest_name)
            quest=request.POST.get('question')
            option1=request.POST.get('option1')
            option2=request.POST.get('option2')
            option3=request.POST.get('option3')
            try:

                quest_obj=Questions.objects.get(relation=quiz,question=quest)
                quest_obj.question=quest
                quest_obj.option1=option1
                quest_obj.option2=option2
                quest_obj.option3=option3
                quest_obj.save()
                return HttpResponseRedirect('/quiz/modify')
            except:
            
                quest_obj=Questions()
                quest_obj.relation=quiz
                quest_obj.question=quest
                quest_obj.option1=option1
                quest_obj.option2=option2
                quest_obj.option3=option3
                quest_obj.save()
                return HttpResponseRedirect('/quiz/modify')
            


            return HttpResponseRedirect('/quiz/modify')

    else:

        id_modify=request.session['id']
        quiz=Quiz.objects.get(id=id_modify)
        quiz_name=quiz.name_quiz
        questions=Questions.objects.filter(relation=quiz)
        return render(request,'Quiz/modify.html',{'questions':questions,'quiz_name':quiz_name,})


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