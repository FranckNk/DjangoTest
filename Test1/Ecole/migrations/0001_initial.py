# Generated by Django 4.1.1 on 2022-10-05 16:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('BI', 'Other')], default='M', max_length=5)),
                ('birthday', models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2015)])),
                ('register_date', models.IntegerField(default=2020, validators=[django.core.validators.MinValueValidator(2018), django.core.validators.MaxValueValidator(2022)])),
                ('New_student', models.BooleanField(default=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('birthday', models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2015)])),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('BI', 'Other')], default='M', max_length=5)),
            ],
        ),
    ]