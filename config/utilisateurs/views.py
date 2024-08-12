# views.py
from rest_framework import viewsets
from .models import Personnel, PersonelAdministratif, PersonnelMedical
from .serializers import PersonnelSerializer, PersonelAdministratifSerializer, PersonnelMedicalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class PersonnelViewSet(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

class PersonelAdministratifViewSet(viewsets.ModelViewSet):
    queryset = PersonelAdministratif.objects.all()
    serializer_class = PersonelAdministratifSerializer

class PersonnelMedicalViewSet(viewsets.ModelViewSet):
    queryset = PersonnelMedical.objects.all()
    serializer_class = PersonnelMedicalSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        personnel = Personnel.objects.get(user=user)
        # personnel = Personnel.objects.filter(personne=personne).first()

        serializer = PersonnelSerializer(personnel)
        return Response(serializer.data)