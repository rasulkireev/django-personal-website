# Generated by Django 2.2.4 on 2019-11-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='intro_thoughts',
            field=models.TextField(blank=True),
        ),
    ]
