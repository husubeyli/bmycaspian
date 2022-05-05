# Generated by Django 3.2.7 on 2021-09-14 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_websitesettings_promotion_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, null=True)),
                ('order', models.IntegerField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='projects/')),
                ('tags', models.JSONField(default=list)),
            ],
        ),
    ]
