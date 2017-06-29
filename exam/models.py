# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class questions(models.Model):
    que = models.CharField(max_length=255)
    opt1 = models.CharField(max_length=255)
    opt2 = models.CharField(max_length=255)
    opt3 = models.CharField(max_length=255)
    opt4 = models.CharField(max_length=255)
    corr_opt = models.CharField(max_length=255)
    test_title = ForeignKey('exam.tests', related_name=test_questions)

class tests(models.Model):
    test_name = models.CharField(max_length=255)
    test_level = models.CharField(max_length=255)
    test_sub = ForeignKey('exam.subjects', related_name='test_subject')

class subjects(models.Model):
    name = models.CharField(max_length=255)
