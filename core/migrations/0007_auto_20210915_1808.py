# Generated by Django 3.2.7 on 2021-09-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_projects_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.IntegerField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='clients/')),
            ],
        ),
        migrations.RemoveField(
            model_name='projects',
            name='url',
        ),
        migrations.RemoveField(
            model_name='service',
            name='url',
        ),
    ]
