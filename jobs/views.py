from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from jobs.models import Category, Job, Application, Review
from jobs.serializers import CategorySerializer, ApplicationSerializer, ReviewSerializer
from jobs.serializers import JobSerializer, CategoryDetailSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework import mixins
from rest_framework import generics


class CategoryList(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class jobList(mixins.ListModelMixin,
            generics.GenericAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class JobDetail(mixins.RetrieveModelMixin,
                generics.GenericAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ApplicationAPIView(APIView):
    permission_classes=[IsAuthenticated, ]

    def post(self, request, id):
        job = get_object_or_404(Job, id=id)
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            full_name = serializer.validated_data.get('full_name')
            email = serializer.validated_data.get('email')
            phone = serializer.validated_data.get('phone')
            upload_cv = serializer.validated_data.get('upload_cv')
            coverletter = serializer.validated_data.get('coverletter')
            created_at = serializer.validated_data.get('created_at')
            is_active = serializer.validated_data.get('is_active')
            is_watch = serializer.validated_data.get('is_watch')

            already_exists = job.application.filter(user=user).exists()
            
            if already_exists:
                content = {'detail': 'Заявка уже отправлена на вакансию'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            
            else:
                application = Application.objects.create(job=job, user=user, full_name=full_name, email=email,
                phone=phone, upload_cv=upload_cv, coverletter=coverletter, 
                created_at=created_at, is_active=is_active, is_watch=is_watch)
                serializer = ApplicationSerializer(instance=application)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReviewAPIView(APIView):
    permission_classes=[IsAuthenticated, ]

    def post(self, request, id):
        job = get_object_or_404(Job, id=id)
        serializer = ReviewSerializer(data=request.data)
        
        if serializer.is_valid():
            user = request.user
            name = serializer.validated_data.get('name')
            comment = serializer.validated_data.get('comment')
            created_at = serializer.validated_data.get('created_at')
            is_active = serializer.validated_data.get('is_active')

            already_exists = job.review_set.filter(user=user).exists()
            
            if already_exists:
                content = {'detail': 'Отзыв уже добавлен!'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            
            else:
                review = Review.objects.create(job=job, user=user, name=name, comment=comment,
                                                created_at=created_at, is_active=is_active)
                serializer = ReviewSerializer(instance=review)
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_job_application(request, pk):
#     job = Job.objects.get(pk=pk)
#     user = request.user
#     data = request.data
#     # SCENERIO

#     #1 Application ALREADY EXIST
#     alreadyExists = job.application.filter(user=user).exists()

#     if alreadyExists:
#         content = {'detail': 'Заявка уже отправлена на вакансию'}
#         return Response(content, status=status.HTTP_400_BAD_REQUEST)

# #2 CREATE Application
#     else:
#         application = Application.objects.create(
#             job=job,
#             user=user,
#             full_name=data['full_name'],
#             email=data['email'],
#             phone=data['phone'],
#             upload_cv=data['upload_cv'],
#             coverletter=data['coverletter']
#         )
#         serializer = ApplicationSerializer(instance=application)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_job_review(request, pk):
#     job = Job.objects.get(pk=pk)
#     user = request.user
#     data = request.data
#     # SCENERIO

#     #1 REVIEW ALREADY EXIST
#     alreadyExists = job.review_set.filter(user=user).exists()

#     if alreadyExists:
#         content = {'detail': 'Отзыв уже добавлен!'}
#         return Response(content, status=status.HTTP_400_BAD_REQUEST)

# #3 CREATE REVIEW
#     else:
#         review = Review.objects.create(
#             job=job,
#             user=user,
#             name=user.first_name,
#             comment=data['comment']
#         )
#         serializer = ReviewSerializer(instance=review)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


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
