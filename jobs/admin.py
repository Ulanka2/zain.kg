from django.contrib import admin

from .models import *


admin.site.register(Application)
admin.site.register(Review)

class JobAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name')
    # list_display_links = ('id', 'name')
    # search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Job, JobAdmin)