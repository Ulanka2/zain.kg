from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'full_name', 'phone', 'upload_cv', 'is_active', 'is_watch', 'created_at')
    list_display_links = ('id', 'job', 'full_name', 'upload_cv', 'is_active', 'is_watch')
    search_fields = ('full_name',)

admin.site.register(Application, ApplicationAdmin)