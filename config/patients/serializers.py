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
class OperationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'
class ExamenSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = '__all__'

class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = '__all__'
class PrescriptionSerialiser(serializers.ModelSerializer):
    operation = OperationSerialiser()
    medicament = MedicamentSerializer()
    examen = ExamenSerialiser()
    class Meta:
        model = Prescription
        fields = '__all__' 

class DiagnosticSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = '__all__'
class ConsultationSerializer(serializers.ModelSerializer):
    diagnostic = DiagnosticSerialiser()
    class Meta:
        model = Consultation
        fields = '__all__'
        
    def create(self, validated_data):
        # recuperation des donnee valider
        diagnostic_data = validated_data.pop('diagnostic')
        if diagnostic_data:
            diagnostic = Diagnostic.objects.create(**diagnostic_data)
        consultation = Consultation.objects.create(diagnostic=diagnostic, **validated_data)
        return consultation
             
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = '__all__'
class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = '__all__'
class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'