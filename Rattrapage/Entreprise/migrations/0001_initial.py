# Generated by Django 4.1.5 on 2023-01-17 05:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(default='nom', max_length=70)),
                ('Location', models.CharField(default='Bathurst', max_length=70)),
                ('ServiceOffert', models.CharField(default='Bathurst', max_length=70)),
                ('Departement', models.CharField(default='Bathurst', max_length=70)),
                ('Type', models.CharField(choices=[('PME', 'Pme'), ('GE', 'Ge'), ('O', 'Other')], default='M', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(default='nom', max_length=70)),
                ('Prenom', models.CharField(default='prenom', max_length=70)),
                ('Age', models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('sexe', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('BI', 'Other')], default='M', max_length=5)),
                ('Poste', models.CharField(default='prenom', max_length=70)),
                ('Salaire', models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('Departement', models.CharField(default='', max_length=20)),
                ('Entreprise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Entreprise.entreprise')),
            ],
        ),
    ]
