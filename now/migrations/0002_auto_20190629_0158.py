# Generated by Django 2.2.2 on 2019-06-29 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('now', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.DateField(blank=True, null=True),
        ),
    ]
