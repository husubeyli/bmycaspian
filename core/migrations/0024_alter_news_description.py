# Generated by Django 3.2.7 on 2021-09-20 23:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
