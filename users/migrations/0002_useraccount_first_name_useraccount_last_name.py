# Generated by Django 5.1.6 on 2025-02-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
