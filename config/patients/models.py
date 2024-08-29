import datetime
from django.db import models
from utilisateurs.models import *

# Create your models here.

# definition du models rendez-vous
class DossierMedical(models.Model):
    dateCreatetion = models.DateField(auto_now=True)
    antecedentsMedicaux = models.TextField(blank=True, max_length=1000)
    alergies = models.TextField(blank=True, max_length=1000)
    medicamentEncoure = models.TextField(blank=True, max_length=1000, null= True)
    groupeSanguin = models.TextField(max_length=10)
    note = models.TextField(blank=True, max_length=1000)
    
class Patient(models.Model):
    personnel = models.ForeignKey(Personnel, related_name='patients', on_delete=models.CASCADE)
    dossier = models.OneToOneField(DossierMedical, related_name='dossier', on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    dateNaissance = models.DateField()
    telephone = models.CharField(max_length=15)
    adresse = models.CharField(max_length=200)
    sexe =  models.CharField(max_length=20, choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')])
    adresseEmail = models.EmailField(blank=True, null=True)
    poids = models.IntegerField()
    taille = models.IntegerField()
    tension_art =  models.IntegerField()
    pouls = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nom
class Diagnostic(models.Model):
    diagnostic = models.CharField(max_length=1000)
    # consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name="diagnosticConcerner")
    
class Consultation(models.Model):
    dateConsultation = models.DateField(auto_now_add=True)
    motif = models.CharField(max_length=200)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='consultations')
    symptome = models.TextField(max_length=200)
    dureeSymptome = models.IntegerField()
    # prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    diagnostic = models.ForeignKey(Diagnostic, on_delete=models.CASCADE) 

class Prescription(models.Model):
    datePrescription = models.DateField(auto_now_add=True)
    medecin = models.ForeignKey(PersonnelMedical, on_delete=models.CASCADE)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)

class Examen(models.Model):
    typeExamen = models.CharField(max_length=100)
    consigne = models.TextField(blank=True, max_length=1000)
    prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE)

    
class Medicament(models.Model):
    nomMedicament = models.TextField(max_length=1000)
    duree = models.CharField(max_length=100)
    dosage = models.TextField(blank=True, max_length=100)
    prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE)    
class Operation(models.Model):
    typeOperation = models.TextField(max_length=200)
    dateOperation = models.DateField()
    delaisDateOperation = models.DateField() # delais pour effectuer l'operation
    prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE)
    
# definition u model de rendez-vous    
class RendezVous(models.Model):
    date_heure = models.DateTimeField(default=datetime.datetime.now)
    actif = models.BooleanField(default=True)
    datePriseRendezVous = models.DateField(auto_now=True)
    motif = models.TextField(max_length=200)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patientConcerner")
    medecin = models.ForeignKey(PersonnelMedical, on_delete=models.CASCADE, related_name="medecinConcerner")