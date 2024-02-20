from django.shortcuts import render
from django.views import generic
from . models import post_model
# Create your views here.

class homeView(generic.ListView):
    model = post_model
    template_name = 'post/index.html'
    context_object_name = 'posts'