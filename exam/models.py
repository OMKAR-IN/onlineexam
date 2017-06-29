# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class question(models.Model):
    que = models.CharField(max_length=255)
    opt1 = models.CharField(max_length=255)
    opt2 = models.CharField(max_length=255)
    opt3 = models.CharField(max_length=255)
    opt4 = models.CharField(max_length=255)
    corr_opt = models.CharField(max_length=255)
    test_title = models.ForeignKey('exam.test', related_name='test_questions')

    def __str__(self):
        return self.que

class test(models.Model):
    test_name = models.CharField(max_length=255)
    test_level = models.CharField(max_length=255)
    test_sub = models.ForeignKey('exam.subject', related_name='test_subject')

    def __str__(self):
        return self.test_name

class subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
