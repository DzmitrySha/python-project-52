# Generated by Django 4.1.1 on 2022-11-07 18:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created date')),
            ],
        ),
        migrations.DeleteModel(
            name='Labels',
        ),
    ]