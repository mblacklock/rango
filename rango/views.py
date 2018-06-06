# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Rango says hey... <br><a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Here is the about page... <br><a href='/rango/'>Index</a>")
