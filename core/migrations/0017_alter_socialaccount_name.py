# Generated by Django 3.2.7 on 2021-09-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_socialaccount_teammember_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
