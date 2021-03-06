# Generated by Django 2.2.4 on 2019-12-06 14:40

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('writings', '0009_auto_20191110_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
