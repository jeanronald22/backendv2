from django.contrib import admin
from .models import *

# Register your models here.
# class d'adminsitrations des differents models
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ['dateNaissance', 'telephone', 'adresse']

class PersonnelAdministratifAdmin(admin.ModelAdmin):
    list_display = ['poste', 'dateEntre', 'isAdmin']
    
class PersonnelMedicalAdmin(admin.ModelAdmin):
    list_display = ['specialite', 'isDoctore']
    
admin.site.register(Personnel,PersonnelAdmin)
admin.site.register(PersonelAdministratif,PersonnelAdministratifAdmin)
admin.site.register(PersonnelMedical, PersonnelMedicalAdmin)