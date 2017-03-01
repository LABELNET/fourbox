# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-28 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='no found doc')),
                ('status', models.IntegerField(default=0, max_length=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('week_num', models.IntegerField(default=0, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cn_name', models.CharField(max_length=15)),
                ('en_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='doc',
            name='Staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='fourbox.Staff'),
        ),
    ]