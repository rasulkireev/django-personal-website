# Generated by Django 2.2.9 on 2020-02-10 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emails',
            new_name='Email',
        ),
    ]
