from django.contrib import admin
from .models import Quiz,Questions,User_Info,Feedback,Test_Score

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(User_Info)
admin.site.register(Test_Score)
admin.site.register(Feedback)

