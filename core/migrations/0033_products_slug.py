# Generated by Django 3.2.7 on 2021-09-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_products_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
