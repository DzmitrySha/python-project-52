# Generated by Django 4.1.1 on 2022-11-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_label_delete_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Name'),
        ),
    ]
