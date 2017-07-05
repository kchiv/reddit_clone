from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^create/', views.create, name='create'),
    url(r'(?P<pk>[0-9]+)/upvote/', views.upvote, name='upvote'),
]
