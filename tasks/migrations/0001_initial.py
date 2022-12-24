# Generated by Django 4.1.1 on 2022-12-24 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labels', '0001_initial'),
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labels.tasklabels')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('executor', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executors', to=settings.AUTH_USER_MODEL, verbose_name='Executor')),
                ('labels', models.ManyToManyField(blank=True, related_name='labels', through='tasks.Relations', to='labels.tasklabels', verbose_name='Labels')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='statuses.taskstatus', verbose_name='Status')),
            ],
        ),
        migrations.AddField(
            model_name='relations',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]
