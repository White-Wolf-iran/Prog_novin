# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import HeaderTitle, WelcomeText
# Create your views here.
def index(request):
	Header = HeaderTitle.objects.all()
	Text = WelcomeText.objects.all()
    return render(request, 'index.html'), {'Header' : Header}, {'Text' : Text})