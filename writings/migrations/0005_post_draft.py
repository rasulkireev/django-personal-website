# Generated by Django 2.2.3 on 2019-08-14 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0004_auto_20190807_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]
