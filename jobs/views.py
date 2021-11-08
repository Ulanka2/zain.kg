from django.db.models.query import QuerySet
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from jobs.models import Category, Job, Application, Review
from jobs.serializers import CategorySerializer, ApplicationSerializer, ReviewSerializer, JobSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404

class CategoryAPIView(APIView):
    
    def get(self, request):
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)


class CategoryDetailAPIView(APIView):
    
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        jobs = Job.objects.filter(category=category)
        serializers = JobSerializer(jobs, many=True)
        return Response(serializers.data)


class jobAPIView(APIView):
    
    def get(self, request):
        jobs = Job.objects.all()
        serializers = JobSerializer(jobs, many=True)
        return Response(serializers.data)


class JobDetailAPIView(APIView):
    
    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        serializers = JobSerializer(job)
        return Response(serializers.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_job_application(request, pk):
    job = Job.objects.get(pk=pk)
    user = request.user
    data = request.data
    # SCENERIO

    #1 Application ALREADY EXIST
    alreadyExists = job.application_set.filter(user=user).exists()

    if alreadyExists:
        content = {'detail': 'The application has already been sent to the vacancy'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

#2 CREATE Application
    else:
        application = Application.objects.create(
            job=job,
            user=user,
            full_name=data['full_name'],
            email=data['email'],
            phone=data['phone'],
            upload_cv=data['upload_cv'],
            coverletter=data['coverletter'],
        )
        return Response('Application Added')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_job_review(request, pk):
    job = Job.objects.get(pk=pk)
    user = request.user
    data = request.data
    # SCENERIO

    #1 REVIEW ALREADY EXIST
    alreadyExists = job.review_set.filter(user=user).exists()

    if alreadyExists:
        content = {'detail': 'Job already Reviewed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

#3 CREATE REVIEW
    else:
        review = Review.objects.create(
            job=job,
            user=user,
            name=user.first_name,
            comment=data['comment']
        )
        serializer = ReviewSerializer(instance=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all().order_by('-id')
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser,]

    @action(methods=['post',], detail=True)
    def is_active(self, request, pk=None):
        review = self.get_object()
        review.is_active = not review.is_active
        review.save()
        serializer = self.get_serializer(instance=review)
        return Response(serializer.data)













# from django.shortcuts import render
# def index(request):
#     return render(request, 'index.html')

# def contact(request):
#     return render(request, 'contact.html')

# def jobs(request):
#     return render(request, 'jobs.html')

# def candidate(request):
#     return render(request, 'candidate.html')

# def job_details(request):
#     return render(request, 'job_details.html')

# def blog(request):
#     return render(request, 'blog.html')
