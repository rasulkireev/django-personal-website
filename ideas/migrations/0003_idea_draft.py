# Generated by Django 2.2.4 on 2019-08-16 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_idea_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
