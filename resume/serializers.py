from rest_framework import serializers
from .models import LanguageChoices, PersonalData, Language, Education, WorkExperience, Skills, LanguageChoices


class PersonalDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PersonalData
        fields = ['id', 'image', 'position_applied_for', 'num_passport_expire', 'full_name', 
                'nationality_gender', 'country_city_of_residence', 'date_and_place_of_birth', 
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
        fields = ['id', 'personal_data', 'university', 'specialization', 
                        'duration', 'year_of_graduation_city_country']
        read_only_fields = ['personal_data', ]
   

class WorkExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkExperience
        fields = ['id', 'personal_data', 'position', 'company_name', 'period_city_country', 'responsibilities']
        read_only_fields = ['personal_data', ]


class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = ['id', 'personal_data', 'other_professional_achievements_skills', 'work_time', 
                                'i_confirm_that_the_information_of_application_form_is_true']
        read_only_fields = ['personal_data', ]