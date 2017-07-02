# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User

# Create your views here.

def signup(request):
	if request.method == 'POST':
		# getting user entered info
		u_name = request.POST['username']
		u_email = request.POST['email']
		u_passwrd_one = request.POST['password1']
		u_passwrd_two = request.POST['password2']
		# success and error messages
		error = 'Passwords didn\'t match.'
		error_name = 'You need to provide a username.'
		success = 'Your account has been created!'
		if u_name == '':
			# throw error if no username provided
			return render(request, 'accounts/signup.html', {'error_name':error_name})
		else:
			if u_passwrd_one != u_passwrd_two:
				# if passwords don't match return error
				return render(request, 'accounts/signup.html', {'error':error})
			else:
				# if passwords do match create new User object
				User.objects.create_user(username=u_name,
										email=u_email,
										password=u_passwrd_one)
				return render(request, 'accounts/signup.html', {'success':success})
	else:
		# if not POST method GET template
		return render(request, 'accounts/signup.html')