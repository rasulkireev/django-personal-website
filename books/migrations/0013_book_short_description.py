# Generated by Django 2.2.4 on 2019-12-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20191226_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='short_description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
