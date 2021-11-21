from os import name
from django.db import models


class PersonalData(models.Model):
    image = models.ImageField(upload_to='image_rezume', null=True, blank=True)
    position_applied_for = models.CharField(max_length=55)
    num_passport_expire = models.CharField(max_length=55)
    full_name = models.CharField(max_length=55)
    nationality_gender = models.CharField(max_length=55)
    country_city_of_residence = models.CharField(max_length=55)
    date_and_place_of_birth = models.CharField(max_length=55)
    age_height_weight = models.CharField(max_length=30)
    status_children = models.CharField(max_length=30)
    health_smoker = models.CharField(max_length=30)
    image_full_height = models.ImageField(upload_to='image_rezume', null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class LanguageChoices(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Language(models.Model):
    language = models.ForeignKey(LanguageChoices, on_delete=models.CASCADE)
    personal_data = models.ForeignKey(PersonalData, on_delete=models.CASCADE)
    LEVEL = [
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    written = models.CharField(max_length=1, choices=LEVEL)
    spoken = models.CharField(max_length=1, choices=LEVEL)
    understanding = models.CharField(max_length=1, choices=LEVEL)


class Education(models.Model):
    personal_data = models.ForeignKey(PersonalData, on_delete=models.CASCADE)
    university = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    duration =  models.CharField(max_length=10)
    year_of_graduation_city_country = models.CharField(max_length=55)
   

class WorkExperience(models.Model):
    personal_data = models.ForeignKey(PersonalData, on_delete=models.CASCADE)
    position = models.CharField(max_length=30)
    company_name = models.CharField(max_length=55)
    period_city_country = models.CharField(max_length=55)
    responsibilities = models.TextField()


class Skills(models.Model):
    personal_data = models.ForeignKey(PersonalData, on_delete=models.CASCADE)
    other_professional_achievements_skills = models.TextField()
    
    I_AM_WILLING_TO_WORK = [
        ('Less than 40 hours/week', 'Less than 40 hours/week'),
        ('40–50 hours/week', '40–50 hours/week'),
        ('More than 50 hours/week', 'More than 50 hours/week'),
    ]
    work_time = models.CharField(max_length=30, choices=I_AM_WILLING_TO_WORK)
    
    i_confirm_that_the_information_of_application_form_is_true = models.CharField(max_length=55)  