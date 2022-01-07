from django.contrib import admin
from .models import Job, Category

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')
    list_display_links = ('id', 'name', 'is_active')
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Job, JobAdmin)
