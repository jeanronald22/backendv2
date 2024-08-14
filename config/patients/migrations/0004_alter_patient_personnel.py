# Generated by Django 5.1 on 2024-08-13 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_patient_poids_patient_pouls_patient_taille_and_more'),
        ('utilisateurs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='utilisateurs.personnel'),
        ),
    ]
