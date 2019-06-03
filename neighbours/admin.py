# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Business,Neighbourhood,Profile

admin.site.register(Business)
admin.site.register(Neighbourhood)
admin.site.register(Profile)