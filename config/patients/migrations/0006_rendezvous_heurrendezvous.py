# Generated by Django 5.1 on 2024-08-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_rendezvous'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendezvous',
            name='heurRendezVous',
            field=models.TimeField(default='12:00:00'),
        ),
    ]
