# Generated by Django 3.2.7 on 2021-09-14 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
