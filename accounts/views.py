# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User

# Create your views here.

def signup(request):
	if request.method == 'POST':

	else:
		return render(request, 'accounts/signup.html')