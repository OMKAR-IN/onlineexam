# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=255)),
                ('opt1', models.CharField(max_length=255)),
                ('opt2', models.CharField(max_length=255)),
                ('opt3', models.CharField(max_length=255)),
                ('opt4', models.CharField(max_length=255)),
                ('corr_opt', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=255)),
                ('test_level', models.CharField(max_length=255)),
                ('test_sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_subject', to='exam.subjects')),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='test_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_questions', to='exam.tests'),
        ),
    ]
