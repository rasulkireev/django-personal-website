# Generated by Django 2.2.4 on 2019-12-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=True),
        ),
    ]