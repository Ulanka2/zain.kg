from django.urls import path
from resume.views import Personal_DataAPIView, LanguageAPIView

urlpatterns = [
    path('personal_data/', Personal_DataAPIView.as_view()),
    path('Language', LanguageAPIView.as_view()),
]