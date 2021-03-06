# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.utils import timezone

from . import models
# Create your views here.

@login_required
def create(request):
	if request.method == 'POST':
		post_title = request.POST['title']
		post_url = request.POST['url']
		error = 'You must provide a title and url.'
		if post_title and post_url:
			post = models.Post()
			post.title = post_title
			if post_url.startswith('http://') or post_url.startswith('https://'):
				post.url = post_url
			else:
				post.url = 'http://' + post_url
			post.pub_date = timezone.datetime.now()
			post.author = request.user
			post.save()
			return redirect('home')
		else:
			return render(request, 'posts/create.html', {'error':error})
	else:
		return render(request, 'posts/create.html')

def home(request):
	posts = models.Post.objects.order_by('-votes_total')
	return render(request, 'posts/home.html', {'posts':posts})

def upvote(request, pk):
	if request.method == 'POST':
		post = models.Post.objects.get(pk=pk)
		post.votes_total += 1
		post.save()
		return redirect('home')

def downvote(request, pk):
	if request.method == 'POST':
		post = models.Post.objects.get(pk=pk)
		post.votes_total -= 1
		post.save()
		return redirect('home')