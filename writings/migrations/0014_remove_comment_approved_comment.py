# Generated by Django 2.2.4 on 2019-12-06 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0013_comment_author_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]