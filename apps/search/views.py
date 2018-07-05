# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.apps import apps
User = apps.get_model('home', 'User');
from models import Item
# Create your views here.

def index(request):
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'ingredients': Item.objects.all(),
    }
    return render(request, 'search/index.html', context)

def addItem(request):
    item = Item.objects.addItem(request.POST)
    print item
    return redirect('/search');
