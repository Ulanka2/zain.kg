from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category
from .models import Job, Review, Application


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'      

class ApplicationSerializer(serializers.ModelSerializer):
    application = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Application
        fields = '__all__'

    def get_application(self,obj):
        application = obj.application_set.all()
        return ApplicationSerializer(application, many=True).data


class ReviewSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=False)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['is_active',]
    
    def get_name(self,obj):
        name = obj.user.first_name
        return name


class JobSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Job
        fields = ['id', 'category', 'name', 'country', 'address', 'description', 'image', 'body', 'work_time', 
        'responsibility', 'job_title', 'salary', 'benefits', 'site', 'email', 'phone', 'reviews']
    
    def get_reviews(self,obj):
        reviews = obj.review_set.filter(is_active=True)
        return ReviewSerializer(reviews, many=True).data


    