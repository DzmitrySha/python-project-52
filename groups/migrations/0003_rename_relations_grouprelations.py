# Generated by Django 4.1.1 on 2023-01-16 15:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0002_group_description_alter_group_creator'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Relations',
            new_name='GroupRelations',
        ),
    ]