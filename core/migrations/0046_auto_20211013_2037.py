# Generated by Django 3.2.7 on 2021-10-13 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_websitesettings_whatsapp_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='url_az',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='url_en',
            field=models.URLField(blank=True, null=True),
        ),
    ]
