from rest_framework import serializers
from .models import Category
from .models import Job, Review, Application
from django.contrib.auth import get_user_model

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields =  ['id', 'name', 'slug', 'jobs']



class JobSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)
    # category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Job
        fields = ['id', 'category', 'name', 'slug', 'country', 'address', 'description', 'image', 'body', 
                'work_time', 'responsibility', 'job_title', 'salary', 'benefits', 'site', 'email', 'phone',
                'is_active', 'created_at', 'reviews']
        
    def get_reviews(self,obj):
        reviews = obj.review_set.filter(is_active=True)
        return ReviewSerializer(reviews, many=True).data


class CategoryDetailSerializer(serializers.ModelSerializer):
    jobs = JobSerializer(many=True, read_only=True)
    jobs = serializers.SerializerMethodField(read_only=True)
    
    
    class Meta:
        model = Category
        fields =  ['id', 'name', 'slug', 'jobs']

    def get_jobs(self,obj):
        jobs = obj.jobs.filter(is_active=True)
        return JobSerializer(jobs, many=True).data



class ApplicationSerializer(serializers.ModelSerializer):
    application = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Application
        fields = ['id', 'job', 'user', 'full_name', 'email', 'phone', 'upload_cv', 'coverletter', 
                  'created_at', 'is_active', 'is_watch'] 

    def get_application(self,obj):
        application = obj.application_set.all()
        return ApplicationSerializer(application, many=True).data


class ReviewSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'job', 'user', 'name', 'comment', 'created_at', 'is_active']
        read_only_fields = ['is_active',]
    
    def get_name(self,obj):
        name = obj.user.first_name
        return name
