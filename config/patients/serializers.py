from .models import *
from rest_framework import serializers
from utilisateurs.serializers import PersonnelSerializer
# definition de serialiazers ici 

class DossierSerializer(serializers.ModelSerializer):
    class Meta:
        model = DossierMedical
        fields = '__all__'
        
class PatientSerializer(serializers.ModelSerializer):
    dossier = DossierSerializer()
    class Meta:
        model = Patient
        fields = '__all__'
        
    def create(self, validated_data):
    #    recuperation des informations sur le dossiers medical
        dossier_medical_data = validated_data.pop('dossier')
        if dossier_medical_data:
            dossier = DossierMedical.objects.create(**dossier_medical_data)
        patient =  Patient.objects.create(dossier = dossier, **validated_data)
        return patient
        
        
    def update(self, instance, validated_data):
        dossier_medical_data = validated_data.pop('dossier', None)
        if dossier_medical_data:
            dossier_instance = instance.dossier
            for attr, value in dossier_medical_data.items():
                setattr(dossier_instance, attr, value)
            dossier_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
class RendezVousSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RendezVous
        fields = '__all__'
        
    