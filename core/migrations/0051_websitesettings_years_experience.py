# Generated by Django 3.2.7 on 2022-02-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20220224_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesettings',
            name='years_experience',
            field=models.IntegerField(default=0),
        ),
    ]
