from django.urls import path
from .views import  index, jobs, contact,  blog, base, job_details

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', job_details, name='job_details'),
    path('apply/', jobs, name='jobs'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    path('base', base, name='base'),
]
