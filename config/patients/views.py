from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework import generics

# Create your views here.
class DossierViewSet(viewsets.ModelViewSet):
    queryset = DossierMedical.objects.all()
    serializer_class = DossierSerializer
    
class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
class RendezVousViewSet(viewsets.ModelViewSet):
    serializer_class = RendezVousSerializer
    def get_queryset(self):
        patient_id = self.request.query_params.get('patient')
        if patient_id:
            return RendezVous.objects.filter(patient=patient_id)
        return RendezVous.objects.all()
  
class DiagnosticViewSet(viewsets.ModelViewSet):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerialiser
class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
class MedicamentViewSet(viewsets.ModelViewSet):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer