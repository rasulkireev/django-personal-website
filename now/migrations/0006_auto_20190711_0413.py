# Generated by Django 2.2.3 on 2019-07-11 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('now', '0005_auto_20190703_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='now',
            name='title',
            field=models.DateField(),
        ),
    ]
