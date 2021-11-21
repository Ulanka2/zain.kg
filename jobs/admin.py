from django.contrib import admin
from .models import Job, Category, Application, Review


class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')
    list_display_links = ('id', 'name', 'is_active')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'upload_cv', 'is_active', 'is_watch', 'created_at')
    list_display_links = ('id', 'user', 'full_name', 'upload_cv', 'is_active', 'is_watch')
    search_fields = ('full_name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'comment', 'is_active', 'created_at')
    list_display_links = ('id', 'user', 'name', 'comment', 'is_active')
    search_fields = ('user',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Review, ReviewAdmin)