# Generated by Django 5.1.6 on 2025-03-01 23:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_rename_course_reviewrating_course'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name='reviewrating',
            index=models.Index(fields=['user', 'course'], name='courses_rev_user_id_bbf528_idx'),
        ),
    ]
