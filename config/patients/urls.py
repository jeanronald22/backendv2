from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include
# definitin des diffiernts vues
# definition du routeurs
route = DefaultRouter()
# enregistrement des route
route.register(r'dossier-medical', DossierViewSet)
route.register(r'liste-patients', PatientsViewSet)
route.register(r'rendez-vous', RendezVousViewSet, basename="rendez-vous")
route.register(r'consultation', ConsultationViewSet)
route.register(r'prescription', PrescriptionViewSet)
route.register(r'examen', ExamenViewSet)
route.register(r'medicament', MedicamentViewSet)
route.register(r'operation', OperationViewSet)
route.register(r'diagnostic', DiagnosticViewSet)

urlpattern = [
    path('', include(route.urls)),
    # path('api/patient/rendez-vous/', RendezVousViewSet.as_view(), name='rendezvous-list'),
]
