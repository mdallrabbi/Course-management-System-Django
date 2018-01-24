# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import dr02fs01_inpS1
from .models import dr02fs01_inptS2

admin.site.register(dr02fs01_inpS1)
admin.site.register(dr02fs01_inptS2)