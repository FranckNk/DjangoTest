# Generated by Django 4.1.1 on 2022-12-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donnee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70)),
                ('Valeur', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('register_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
