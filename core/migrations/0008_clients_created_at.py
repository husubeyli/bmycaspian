# Generated by Django 3.2.7 on 2021-09-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210915_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
