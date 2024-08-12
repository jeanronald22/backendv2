# serializers.py
from rest_framework import serializers
from .models import Personnel, PersonelAdministratif, PersonnelMedical
from django.contrib.auth.models import User

# Sérialiseur pour le modèle User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

# Sérialiseur pour le modèle Personnel
class PersonnelSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Personnel
        fields = ['id', 'dateNaissance', 'adresse', 'telephone', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        personnel = Personnel.objects.create(user=user, **validated_data)
        return personnel

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_instance = instance.user
            for attr, value in user_data.items():
                setattr(user_instance, attr, value)
            if 'password' in user_data:
                user_instance.set_password(user_data['password'])
            user_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# Sérialiseur pour le modèle PersonelAdministratif
class PersonelAdministratifSerializer(serializers.ModelSerializer):
    personnel = PersonnelSerializer()

    class Meta:
        model = PersonelAdministratif
        fields = ['id', 'personnel', 'poste', 'dateEntre', 'isAdmin']

    def create(self, validated_data):
        personnel_data = validated_data.pop('personnel')
        user_data = personnel_data.pop('user')
        user = User.objects.create_user(**user_data)
        personnel = Personnel.objects.create(user=user, **personnel_data)
        return PersonelAdministratif.objects.create(personnel=personnel, **validated_data)

    def update(self, instance, validated_data):
        personnel_data = validated_data.pop('personnel', None)
        if personnel_data:
            user_data = personnel_data.pop('user', None)
            if user_data:
                user_instance = instance.personnel.user
                for attr, value in user_data.items():
                    setattr(user_instance, attr, value)
                if 'password' in user_data:
                    user_instance.set_password(user_data['password'])
                user_instance.save()

            personnel_instance = instance.personnel
            for attr, value in personnel_data.items():
                setattr(personnel_instance, attr, value)
            personnel_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# Sérialiseur pour le modèle PersonnelMedical
class PersonnelMedicalSerializer(serializers.ModelSerializer):
    personnel = PersonnelSerializer()

    class Meta:
        model = PersonnelMedical
        fields = ['id', 'personnel', 'specialite', 'isDoctore']

    def create(self, validated_data):
        personnel_data = validated_data.pop('personnel')
        user_data = personnel_data.pop('user')
        user = User.objects.create_user(**user_data)
        personnel = Personnel.objects.create(user=user, **personnel_data)
        return PersonnelMedical.objects.create(personnel=personnel, **validated_data)

    def update(self, instance, validated_data):
        personnel_data = validated_data.pop('personnel', None)
        if personnel_data:
            user_data = personnel_data.pop('user', None)
            if user_data:
                user_instance = instance.personnel.user
                for attr, value in user_data.items():
                    setattr(user_instance, attr, value)
                if 'password' in user_data:
                    user_instance.set_password(user_data['password'])
                user_instance.save()

            personnel_instance = instance.personnel
            for attr, value in personnel_data.items():
                setattr(personnel_instance, attr, value)
            personnel_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
