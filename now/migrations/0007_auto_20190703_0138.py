# Generated by Django 2.2.2 on 2019-07-03 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('now', '0006_auto_20190703_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='now',
            name='title',
            field=models.DateField(),
        ),
    ]
