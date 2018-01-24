# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response

from dp_Directory03.models import Post
from django.http import HttpResponse

from django.views.generic import TemplateView

# Create your views here.

def webview_dpdr03f01(request):
    return render_to_response('dp_dr_03_webfile01.html')

def webview_dpdr03f02(request):
    return render_to_response('dp_dr_03_webfile02.html')
