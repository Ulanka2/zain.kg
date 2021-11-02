from django.urls import path
from .views import index, contact, jobs, candidate, job_details, blog


urlpatterns = [
     path('', index, name='index'),
     path('contact/', contact, name='contact'),
     path('jobs/', jobs, name='jobs'),
     path('candidate/', candidate, name='candidate'),
     path('job_details/', job_details, name='job_details'),
     path('blog/', blog, name='blog'),

]