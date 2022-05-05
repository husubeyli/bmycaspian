# Generated by Django 3.2.7 on 2022-02-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_websitesettings_footer_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_az', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('order', models.IntegerField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='partners/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='partners/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
