# Generated by Django 3.2.7 on 2021-09-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20210929_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesettings',
            name='address_link',
            field=models.URLField(default=False),
            preserve_default=False,
        ),
    ]
