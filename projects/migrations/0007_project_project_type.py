# Generated by Django 2.2.3 on 2019-07-12 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20190711_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('Project', 'Project'), ('Hustle', 'Hustle')], default='Project', max_length=10),
        ),
    ]
