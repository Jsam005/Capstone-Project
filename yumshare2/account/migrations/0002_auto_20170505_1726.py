# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 00:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default-image.png', upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='biography',
            field=models.TextField(blank=True, help_text='Tell us about yourself', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]