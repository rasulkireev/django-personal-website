# Generated by Django 2.2.4 on 2019-12-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0012_auto_20191206_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
