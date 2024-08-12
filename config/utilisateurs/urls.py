# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonnelViewSet, PersonelAdministratifViewSet, PersonnelMedicalViewSet, UserProfileView

router = DefaultRouter()
router.register(r'personnel', PersonnelViewSet)
router.register(r'personel-administratif', PersonelAdministratifViewSet)
router.register(r'personnel-medical', PersonnelMedicalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),
]
