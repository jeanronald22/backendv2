from typing import Any
from django.contrib import admin
from django.urls.resolvers import URLResolver
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

# personnalisation
# class MyAdminSite(admin.AdminSite):
#     def get_urls(self) -> list[URLResolver]:
#         urls =  super().get_urls()
#         custom_urls = [
            
#         ]
#         return urls + custom_urls
        
#     def each_context(self, request: Any) -> Any:
#         context = super().each_context(request)
#         context['additional_css'] ='./static/admin.css'
#         return context
       
# admin.site = MyAdminSite() 
admin.site.site_header=("Doctorer")
admin.site.index_title=("Bienvenue dans l'administration")