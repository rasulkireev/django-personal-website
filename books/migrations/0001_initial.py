# Generated by Django 2.2.3 on 2019-07-21 18:44

import autoslug.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('buylink', models.URLField(blank=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('title',))),
                ('description', models.TextField(blank=True)),
                ('rank', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('cover', models.ImageField(blank=True, upload_to='book-cover/')),
            ],
        ),
    ]
