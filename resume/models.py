from django.db import models


class Personal_Data(models.Model):
    image = models.ImageField(upload_to='media_rezume')#3/4
    position_applied_for = models.CharField(max_length=55)
    num_passport_expire = models.CharField(max_length=55)
    full_name = models.CharField(max_length=55)
    nationality_gender = models.CharField(max_length=55)
    country_city_of_residence = models.CharField(max_length=55)
    date_and_place_of_birth = models.CharField(max_length=55)
    age_height_weight = models.CharField(max_length=30)
    status_children = models.CharField(max_length=30)
    health_smoker = models.CharField(max_length=30)
    image_full_height = models.ImageField(upload_to='media_rezume')#6/4 в полный рост


class Language(models.Model):
    # LANGUAGE = (
    #     ('E', 'English'),
    #     ('R', 'Russian'),
    #     ('T', 'Turkish'),
    #     ('A', 'Arabic'),
    #     ('C', 'Chinese'),
    # )
    language = models.CharField(max_length=10)
    
    # LEVEL = (
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    # )
    written = models.CharField(max_length=1)
    spoken = models.CharField(max_length=1)
    understanding = models.CharField(max_length=1)


class Education(models.Model):
    university = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    duration =  models.CharField(max_length=10)
    year_of_graduation_city_country = models.CharField(max_length=55)
   

class Work_Experience(models.Model):
    position = models.CharField(max_length=30)
    company_name = models.CharField(max_length=55)
    period_city_country = models.CharField(max_length=55)
    responsibilities = models.TextField()


class Skills(models.Model):
    
    other_professional_achievements_skills = models.TextField()
    
    I_AM_WILLING_TO_WORK = (
        ('1', 'Less than 40 hours/week'),
        ('2', '40–50 hours/week'),
        ('3', 'More than 50 hours/week'),
    )
    work_time = models.CharField(max_length=30, choices=I_AM_WILLING_TO_WORK)
    
    i_confirm_that_the_information_of_application_form_is_true = models.CharField(max_length=5)
