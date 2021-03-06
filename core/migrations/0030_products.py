# Generated by Django 3.2.7 on 2021-09-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_projects_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('project_id', models.ManyToManyField(blank=True, to='core.Projects')),
            ],
        ),
    ]
