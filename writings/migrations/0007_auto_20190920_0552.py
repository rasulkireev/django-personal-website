# Generated by Django 2.2.4 on 2019-09-20 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0006_auto_20190815_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Coding', 'Coding'), ('Cooking', 'Cooking'), ('Personal', 'Personal')], default='Personal', max_length=10),
        ),
    ]