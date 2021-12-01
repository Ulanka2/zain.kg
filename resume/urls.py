from django.urls import path
from resume.views import PersonalDataAPIView, LanguageAPIView, EducationAPIView, SkillsAPIView
from resume.views import WorkExperienceOneAPIView, WorkExperienceTwoAPIView, WorkExperienceThreeAPIView

urlpatterns = [
    path('personal_data/', PersonalDataAPIView.as_view()),
    path('<str:id>/language/', LanguageAPIView.as_view()),
    path('<str:id>/education/', EducationAPIView.as_view()),
    path('<str:id>/workexperienceone/', WorkExperienceOneAPIView.as_view()),
    path('<str:id>/workexperiencetwo/', WorkExperienceTwoAPIView.as_view()),
    path('<str:id>/workexperiencethree/', WorkExperienceThreeAPIView.as_view()),
    path('<str:id>/skills/', SkillsAPIView.as_view()),
]
