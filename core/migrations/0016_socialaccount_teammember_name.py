# Generated by Django 3.2.7 on 2021-09-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_socialaccount_teammember'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialaccount',
            name='teammember_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
