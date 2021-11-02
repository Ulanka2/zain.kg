from django import forms
from django.db import models
from django.db.models import fields

class Personal_DataForm(forms.Form):
    image = forms.ImageField(upload_to='media_rezume')#3/4
    position_applied_for = forms.CharField(max_length=55)
    num_passport_expire = forms.CharField(max_length=55)
    full_name = forms.CharField(max_length=55)
    nationality_gender = forms.CharField(max_length=55)
    country_city_of_residence = forms.CharField(max_length=55)
    date_and_place_of_birth = forms.CharField(max_length=55)
    age_height_weight = forms.CharField(max_length=30)
    status_children = forms.CharField(max_length=30)
    health_smoker = forms.CharField(max_length=30)
    image_full_height = forms.ImageField(upload_to='media_rezume')#6/4 в полный рост


class LanguageForm(forms.Form):
    LANGUAGE = (
        ('E', 'English'),
        ('R', 'Russian'),
        ('T', 'Turkish'),
        ('A', 'Arabic'),
        ('C', 'Chinese'),
    )
    language = forms.CharField(max_length=10, choices=LANGUAGE)
    
    LAVEL = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    written = forms.CharField(max_length=1, choices=LAVEL)
    spoken = forms.CharField(max_length=1, choices=LAVEL)
    understanding = forms.CharField(max_length=1, choices=LAVEL)

class EducationForm(forms.Form):
    university = forms.CharField(max_length=100)
    specialization = forms.CharField(max_length=100)
    duration =  forms.CharField(max_length=10)
    year_of_graduation_city_country = forms.CharField(max_length=55)

class Work_ExperienceForm(forms.Form):
    position = forms.CharField(max_length=30)
    company_name = forms.CharField(max_length=55)
    period_city_country = forms.CharField(max_length=55)
    responsibilities = forms.CharField(widget=forms.Textarea)

class SkillsForm(forms.Form):
    
    other_professional_achievements_skills = forms.CharField(widget=forms.Textarea)
    
    I_AM_WILLING_TO_WORK = (
        ('1', 'Less than 40 hours/week'),
        ('2', '40–50 hours/week'),
        ('3', 'More than 50 hours/week'),
    )
    work_time = forms.CharField(max_length=30, choices=I_AM_WILLING_TO_WORK)
    
    i_confirm_that_the_information_of_application_form_is_true = forms.CharField(max_length=5)



