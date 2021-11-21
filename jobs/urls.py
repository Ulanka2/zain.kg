from rest_framework.routers import SimpleRouter
from jobs.views import CategoryList, CategoryDetail, JobDetail, jobList
from jobs.views import create_job_application, create_job_review
from django.urls import path

router = SimpleRouter()
# router.register('review', ReviewViewSet)
urlpatterns = [
    
    path('category/', CategoryList.as_view()),
    path('<str:pk>/categorydetail/', CategoryDetail.as_view()),
    path('all/', jobList.as_view()),
    path('<str:pk>/detail/', JobDetail.as_view()),
    path('<str:pk>/application/', create_job_application, name='create_application'),
    path('<str:pk>/review/', create_job_review, name='create_review')
]
urlpatterns += router.urls




# from django.urls import path
# from .views import index, contact, jobs, candidate, job_details, blog


# urlpatterns = [
#      path('', index, name='index'),
#      path('contact/', contact, name='contact'),
#      path('jobs/', jobs, name='jobs'),
#      path('candidate/', candidate, name='candidate'),
#      path('job_details/', job_details, name='job_details'),
#      path('blog/', blog, name='blog'),
# ]