# Generated by Django 2.2.3 on 2019-07-06 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20190703_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
