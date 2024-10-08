# Generated by Django 5.1 on 2024-08-20 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0011_remove_prescription_examen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='prescription',
        ),
        migrations.AddField(
            model_name='examen',
            name='prescription',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients.prescription'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicament',
            name='prescription',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients.prescription'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='prescription',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients.prescription'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='consultation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients.consultation'),
            preserve_default=False,
        ),
    ]
