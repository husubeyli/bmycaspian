# Generated by Django 3.2.7 on 2022-02-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_auto_20220224_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpagecontent',
            name='author_position_az',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutpagecontent',
            name='author_position_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]