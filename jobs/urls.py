from rest_framework.routers import SimpleRouter
from jobs.views import CategoryAPIView, CategoryDetailAPIView, JobDetailAPIView, jobAPIView, ReviewViewSet
from jobs.views import create_job_application, create_job_review
from django.urls import path

router = SimpleRouter()
router.register('review', ReviewViewSet)
urlpatterns = [
    
    path('get_category_all/', CategoryAPIView.as_view()),
    path('<str:pk>/get_category/', CategoryDetailAPIView.as_view()),
    path('get_all/', jobAPIView.as_view()),
    path('<str:pk>/get_job_detail/', JobDetailAPIView.as_view()),
    path('<str:pk>/create_application/', create_job_application, name='create_application'),
    path('<str:pk>/create_review/', create_job_review, name='create_review')
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