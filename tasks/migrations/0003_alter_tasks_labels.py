# Generated by Django 4.1.1 on 2022-11-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', through='tasks.Relations', to='labels.label', verbose_name='Labels'),
        ),
    ]
