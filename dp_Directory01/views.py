# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response

# Create your views here.

def webview_dpdr01f01(request):
    return render_to_response('dp_dr_01_webfile01.html')

def webview_dpdr01f02(request):
    return render_to_response('dp_dr_01_webfile02.html')

def webview_dpdr01f03(request):
    return render_to_response('dp_dr_01_webfile03.html')
