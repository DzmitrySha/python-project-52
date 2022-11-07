# Generated by Django 4.1.1 on 2022-11-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_label_delete_labels'),
        ('tasks', '0002_alter_tasks_author_alter_tasks_executor'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='label',
            field=models.ManyToManyField(related_name='labels', to='labels.label', verbose_name='Label'),
        ),
    ]