# Generated by Django 3.2.7 on 2021-09-29 07:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_projects_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
