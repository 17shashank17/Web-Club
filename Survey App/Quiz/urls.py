
from django.urls import path,include
from django.conf.urls import url
from . import views
#from django.conf import settings

urlpatterns = [
    #url(r'^api/v1/',('social_django.urls',namespace='social')),
    url(r'^$',views.home,name="home"),
    url(r'^quizall',views.quiz_all,name="quiz_all"),
    url(r'^(\d+)/$',views.questions,name="questions"),
    url(r'^login',views.login_user,name="login_user"),
    url(r'^signup',views.signup,name="signup"),
    url(r'^logout',views.logout_user,name="logout_user"),
    url(r'^profile',views.profile,name="profile"),
    url(r'^create_quiz',views.create_quiz,name="create_quiz"),
    #url(r'^survey_taken',views.survey_taken,name="survey_taken"),
    url(r'^your_quiz',views.your_quiz,name="your_quiz"),
    url(r'^modify',views.modify_quiz,name="modify_quiz"),
    url(r'^results',views.results,name="results"),
]

#AIzaSyCRNh2DQfCBPzTVKkO9yzA0Yy4JbQq3vVM