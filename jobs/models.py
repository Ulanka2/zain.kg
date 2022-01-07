from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)
              
    def __str__(self):
        return self.name



class Job(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs', verbose_name='Категория')
    name = models.CharField(max_length=200, verbose_name='Название вакансии')
    country = models.CharField(max_length=100, verbose_name='Страна', null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to="jobs_image/%Y/%m/%d/", null=True, blank=True, verbose_name='Изображение')
    body =  RichTextField(null=True, blank=True)
    work_time = models.CharField(max_length=55, null=True, blank=True)
    responsibility = models.TextField(null=True, blank=True, verbose_name='Обязанность')
    salary = models.CharField(max_length=55, null=True, blank=True)
    benefits = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        
    def __str__(self):
        return self.name

