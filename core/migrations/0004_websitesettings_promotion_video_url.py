# Generated by Django 3.2.7 on 2021-09-14 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_websitesettings_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesettings',
            name='promotion_video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
