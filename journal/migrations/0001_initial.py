# Generated by Django 2.2.3 on 2019-08-08 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('topic', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
        ),
    ]
