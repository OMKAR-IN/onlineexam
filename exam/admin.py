# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import question , test , subject

admin.site.register(subject)
admin.site.register(test)
admin.site.register(question)
