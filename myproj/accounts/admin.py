from django.contrib import admin
from .models import PersonalDetails,AcademicDetails
# Register your models here.

admin.site.register(PersonalDetails)
admin.site.register(AcademicDetails)