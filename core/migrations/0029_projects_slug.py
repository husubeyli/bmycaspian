# Generated by Django 3.2.7 on 2021-09-29 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_websitesettings_promotion_video_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]