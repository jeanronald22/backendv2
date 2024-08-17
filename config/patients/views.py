from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

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
        queryset = RendezVous.objects.all()
        medecin_id = self.request.query_params.get('medecin_id')
        if medecin_id is not None:
            queryset = queryset.filter(medecin_id=medecin_id)
        return queryset
   
