# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Article
from datetime import datetime

# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" 
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)

def test(request) :
#    return render(request, 'test.html', {'current_time': datetime.now()})
#render(request, template_name, context=None, content_type=None, status=None, using=None)
     return render(request, 'home.html',{'post_list':Article.objects.all()})

def index(request) :
     return render(request, 'index.html')
