# Generated by Django 2.2.4 on 2019-12-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20191213_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='book-cover/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_read',
            field=models.DateField(blank=True),
        ),
    ]
