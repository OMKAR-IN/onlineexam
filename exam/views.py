# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import question, test, subject
from django.shortcuts import render

# Create your views here.
def tests_list(request):
    tests = test.objects.all()
    return render(request, 'test_templates/all_tests.html', {'tests': tests})
