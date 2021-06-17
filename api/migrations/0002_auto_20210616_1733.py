# Generated by Django 3.2.4 on 2021-06-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='duration',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
