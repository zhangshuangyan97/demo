# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-07-12 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=128)),
                ('icon', models.ImageField(upload_to='')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('M', '男'), ('F', '女'), ('U', '保密')], max_length=8)),
            ],
        ),
    ]
