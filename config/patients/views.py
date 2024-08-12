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
    