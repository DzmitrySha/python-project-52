# Generated by Django 4.1.1 on 2022-10-29 20:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created date')),
            ],
        ),
    ]
