from django.contrib import admin
from .models import PersonalData, LanguageChoices

class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position', 'file', 'created_at')
    list_display_links = ('id', 'full_name', 'position', 'file')
    search_fields = ('full_name',)

class LanguageChoicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

admin.site.register(PersonalData, PersonalDataAdmin)
admin.site.register(LanguageChoices, LanguageChoicesAdmin)



