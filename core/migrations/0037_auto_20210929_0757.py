# Generated by Django 3.2.7 on 2021-09-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_projects_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='projectstatistics',
            name='icon',
            field=models.CharField(max_length=100),
        ),
    ]