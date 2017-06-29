# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import questions, tests, subjects
from django.shortcuts import render

# Create your views here.
def tests_list(request):
    test = tests.objects.all()
    return render(request, 'base.html', {'tests': tests})
