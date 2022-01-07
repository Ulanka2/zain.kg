from django.db import models
from jobs.models import Job

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.SET_NULL,null=True, related_name='application')
    full_name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=55, null=True, blank=True)
    upload_cv = models.FileField(upload_to="rezume_apply/%Y/%m/%d/")
    coverletter = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_watch = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заявка на вакансию'
        verbose_name_plural = 'Заявки на вакансию'
        ordering = ['-created_at']
        
    def __str__(self):
        return f'Заявка от {self.full_name}'
