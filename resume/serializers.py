from rest_framework import serializers

class Personal_DataSerializer(serializers.Serializer):
    image = serializers.ImageField()#3/4
    position_applied_for = serializers.CharField(max_length=55)
    num_passport_expire = serializers.CharField(max_length=55)
    full_name = serializers.CharField(max_length=55)
    nationality_gender = serializers.CharField(max_length=55)
    country_city_of_residence = serializers.CharField(max_length=55)
    date_and_place_of_birth = serializers.CharField(max_length=55)
    age_height_weight = serializers.CharField(max_length=30)
    status_children = serializers.CharField(max_length=30)
    health_smoker = serializers.CharField(max_length=30)
    image_full_height = serializers.ImageField()#6/4 в полный рост
# Сигнатура: ImageField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL)

class LanguageSerializer(serializers.Serializer):
    LANGUAGE = ['English', 'Russian', 'Turkish', 'Arabic', 'Chinese']
    language = serializers.ChoiceField(choices=LANGUAGE)
    
    LAVEL = [1, 2, 3, 4, 5]
    written = serializers.ChoiceField(choices=LAVEL)
    spoken = serializers.ChoiceField(choices=LAVEL)
    understanding = serializers.ChoiceField(choices=LAVEL)
    


class EducationSerializer(serializers.Serializer):
    university = serializers.CharField(max_length=100)
    specialization = serializers.CharField(max_length=100)
    duration =  serializers.CharField(max_length=10)
    year_of_graduation_city_country = serializers.CharField(max_length=55)
   

class Work_ExperienceSerializer(serializers.Serializer):
    position = serializers.CharField(max_length=30)
    company_name = serializers.CharField(max_length=55)
    period_city_country = serializers.CharField(max_length=55)
    responsibilities = serializers.CharField(max_length=300)


class SkillsSerializer(serializers.Serializer):
    
    other_professional_achievements_skills = serializers.CharField(max_length=300)
    
    I_AM_WILLING_TO_WORK = ['Less than 40 hours/week', '40–50 hours/week', 'More than 50 hours/week']
    work_time = serializers.ChoiceField(choices=I_AM_WILLING_TO_WORK)
    
    i_confirm_that_the_information_of_application_form_is_true = serializers.CharField(max_length=5)