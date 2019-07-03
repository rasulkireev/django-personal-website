# Generated by Django 2.2.2 on 2019-07-03 01:34

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('now', '0005_auto_20190703_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='now',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='now',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
