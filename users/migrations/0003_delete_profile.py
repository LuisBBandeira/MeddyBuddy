# Generated by Django 5.1.2 on 2024-11-09 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_health_card'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]