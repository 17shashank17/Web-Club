
from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home,name="home"),
    url(r'^quizall',views.quiz_all,name="quiz_all"),
    url(r'^(\d+)/$',views.questions,name="questions"),
    url(r'^login',views.login_user,name="login_user"),
    url(r'^signup',views.signup,name="signup"),
    url(r'^logout',views.logout_user,name="logout_user"),
    url(r'^profile',views.profile,name="profile"),
    url(r'^create_quiz',views.create_quiz,name="create_quiz"),
]