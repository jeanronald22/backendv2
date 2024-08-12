from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # definiton d'une relation un a un entre le model User de django et mon model personnel
    dateNaissance = models.DateField()
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=15)
    
    def __str__(self): # redefiniton de la fonction String
        return self.user.username

class PersonelAdministratif(models.Model):
    personnel = models.OneToOneField(Personnel, on_delete=models.CASCADE)
    poste = models.CharField(max_length=50)
    dateEntre = models.DateField()
    isAdmin = models.BooleanField(default= False)
    
    def __str__(self):
        return self.personnel.user.username

class PersonnelMedical(models.Model):
    personnel = models.OneToOneField(Personnel, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=50)
    isDoctore = models.BooleanField(default=False)
    