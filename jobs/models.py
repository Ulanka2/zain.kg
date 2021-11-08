from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)
              
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('job_list_by_category', args=[self.slug])


class Job(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs',verbose_name='Категория')
    name = models.CharField(max_length=200, verbose_name='Название вакансии')
    slug = models.SlugField(max_length=200, unique=True)
    country = CountryField(blank_label='(select country)')
    address = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='media_job', null=True, blank=True, verbose_name='Изображение')
    body =  RichTextField(null=True, blank=True)
    work_time = models.CharField(max_length=55, null=True, blank=True)
    responsibility = models.TextField(null=True, blank=True, verbose_name='Обязанность')
    job_title = models.CharField(max_length=55, null=True, blank=True, verbose_name='Должность')
    salary = models.CharField(max_length=55, null=True, blank=True)
    benefits = models.TextField(null=True, blank=True)
    site = models.URLField(null=True, blank=True, verbose_name='Сайт компании')
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=55, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('job_details', args=[self.id, self.slug])


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=55, null=True, blank=True)
    upload_cv = models.FileField(upload_to='media_rezume')
    coverletter = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_watch = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заявка на вакансию'
        verbose_name_plural = 'Заявки на вакансию'
        ordering = ['-created_at']
        
    def __str__(self):
        return f'Заявка от {self.user}, {self.full_name}'


class Review(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы от кандидатов'
        ordering = ['-created_at']
        
    def __str__(self):
        return f'Отзыв от {self.user}'





    
