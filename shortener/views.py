#!/usr/bin/env python
""" views
"""
from django.shortcuts import render
from .models import ShortUrl
from django.shortcuts import redirect, get_object_or_404
# Create your views here.

def index(request):
    """ index route
    """
    if request.method == "POST":
        data = request.POST
        name = data['name']
        url = data['url']

        shorturl = ShortUrl.objects.create(name=name, url=url)
        print("Short URL created")

    context = {}
    template = "index.html"
    return render(request, template, context)

def rerouter(request, name):
    """ redirects urls
    """
    url = get_object_or_404(ShortUrl, name=name)
    return redirect(url.url)