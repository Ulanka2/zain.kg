from rest_framework.routers import SimpleRouter
from jobs.views import CategoryList, CategoryDetail, JobDetail, jobList, ApplicationAPIView, ReviewAPIView
from jobs.views import ReviewViewSet
from django.urls import path

router = SimpleRouter()
router.register('reviewadmin', ReviewViewSet)
urlpatterns = [
    
    path('category/', CategoryList.as_view()),
    path('<str:pk>/categorydetail/', CategoryDetail.as_view()),
    path('all/', jobList.as_view()),
    path('<str:pk>/detail/', JobDetail.as_view()),
    # path('<str:pk>/application/', create_job_application, name='create_application'),
    # path('<str:pk>/review/', create_job_review, name='create_review'),
    path('<str:id>/application/', ApplicationAPIView.as_view()),
    path('<str:id>/review/', ReviewAPIView.as_view()),

]
urlpatterns += router.urls
