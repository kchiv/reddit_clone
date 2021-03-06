# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
		error_exists = 'That username already exists.'
		success = 'Your account has been created!'
		if u_name == '':
			# throw error if no username provided
			return render(request, 'accounts/signup.html', {'error_name':error_name})
		else:
			if u_passwrd_one != u_passwrd_two:
				# if passwords don't match return error
				return render(request, 'accounts/signup.html', {'error':error})
			else:
				try:
					User.objects.get(username=u_name)
					return render(request, 'accounts/signup.html', {'error_exists':error_exists})
				except User.DoesNotExist:
					# if passwords do match create new User object
					user = User.objects.create_user(username=u_name,
											email=u_email,
											password=u_passwrd_one)
					login(request, user)
					return render(request, 'accounts/signup.html', {'success':success})
	else:
		# if not POST method GET template
		return render(request, 'accounts/signup.html')

def loginview(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# success and error messages
		error = 'Your username or password is incorrect.'
		error_user = 'You need to provide a username.'
		error_pswd = 'You need to provide a password.'
		success = 'Login successful.'
		user = authenticate(request, username=username, password=password)
		if username == '':
			return render(request, 'accounts/login.html', {'error':error_user})
		elif password == '':
			return render(request, 'accounts/login.html', {'error':error_pswd})
		else:
			if user is not None:
				login(request, user)
				if 'next' in request.POST:
					return redirect(request.POST['next'])
				else:
					return render(request, 'accounts/login.html', {'success':success})
			else:
				return render(request, 'accounts/login.html', {'error':error})
	else:
		return render(request, 'accounts/login.html')

def logoutview(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')
