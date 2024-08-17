from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include
# definitin des diffiernts vues
# definition du routeurs
route = DefaultRouter()
# enregistrement des route
route.register(r'dossier-medical', DossierViewSet)
route.register(r'liste-patients', PatientsViewSet)
route.register(r'rendez-vous', RendezVousViewSet)

urlpattern = [
    path('', include(route.urls))
]
