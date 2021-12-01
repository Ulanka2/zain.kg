from rest_framework import serializers
from .models import LanguageChoices, PersonalData, Language, Education, WorkExperience, Skills, LanguageChoices


class PersonalDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PersonalData
        fields = ['id', 'image', 'position', 'num_passport', 'full_name', 
                'nationality_gender', 'country_city_of_residence', 'date_of_birth', 
        'age_height_weight', 'status_children', 'health_smoker', 'image_full_height', 'file']
    

class LanguageChoicesSerializer(serializers.ModelSerializer):
   
    model = LanguageChoices
    fields = ['id', 'name']


class LanguageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Language
        fields = ['id', 'personal_data', 'language', 'written', 'spoken', 'understanding']
        read_only_fields = ['personal_data', ]
    

class EducationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Education
        fields = ['id', 'personal_data', 'university', 'specialization', 'duration', 'city_country']
        read_only_fields = ['personal_data', ]
   

class WorkExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkExperience
        fields = ['id', 'personal_data', 'position', 'company_name', 'period_city_country', 'responsibilities']
        read_only_fields = ['personal_data', ]


class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = ['id', 'personal_data', 'skills', 'work_time', 'i_confirm']
        read_only_fields = ['personal_data', ]
