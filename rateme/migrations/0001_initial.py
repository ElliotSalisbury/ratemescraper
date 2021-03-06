# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-10 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('body', models.CharField(max_length=4096)),
                ('rating', models.IntegerField()),
                ('decimal', models.FloatField()),
                ('author', models.CharField(max_length=256)),
                ('created', models.DateTimeField()),
                ('permalink', models.URLField()),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('author', models.CharField(max_length=256)),
                ('created', models.DateTimeField()),
                ('permalink', models.URLField()),
                ('score', models.IntegerField()),
                ('upvote_ratio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rateme.Submission')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='rateme.Submission'),
        ),
    ]
