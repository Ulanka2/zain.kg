from django.contrib import admin

from .models import PersonalData, LanguageChoices, Language, Education, WorkExperience, Skills

admin.site.register(PersonalData)
admin.site.register(LanguageChoices)
admin.site.register(Language)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Skills)


