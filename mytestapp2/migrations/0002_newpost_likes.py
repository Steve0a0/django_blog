# Generated by Django 4.1.7 on 2023-08-02 13:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mytestapp2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpost',
            name='likes',
            field=models.ManyToManyField(related_name='blog', to=settings.AUTH_USER_MODEL),
        ),
    ]
