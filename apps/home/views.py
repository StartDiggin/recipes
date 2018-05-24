# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, Recipe, Ingredient

# Create your views here.
def index(request):
    context = {
    'user' : User.objects.get(first_name = request.session['first_name'])
    }
    return render(request, 'home/index.html', context);

def create_user(request):
    user = User.objects.addUser(request.POST)
    request.session['user'] = user.first_name
    return redirect('/');

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        messages.error(request, 'Name not in DB')
        return redirect('/')
    request.session['first_name'] = results['user'].first_name
    return redirect('/');

def create_recipe(request):
    user = request.session['first_name']
    recipe = Recipe.objects.addRecipe(user, request.POST)
    # print recipe.id, "recipe id"
    request.session['curRecipe'] = recipe.id
    # print request.session['curRecipe']
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'curRecipe': Recipe.objects.get(id = recipe.id),
    }
    return redirect('/');

def recipes(request):
    id = request.session['curRecipe']
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'recipes': Recipe.objects.all(),
    # 'curRecipe': Recipe.objects.get(id = id)
    }
    return render(request, 'home/recipePage.html', context);

def add_Ingredient(request, id):
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'curRecipe': Recipe.objects.get(id = id)
    }
    return render(request, 'home/addIngredients.html', context);

def add_ingre_to_recipe(request, id):
    recipe = Recipe.objects.get(id = id)
    ingredient = Ingredient.objects.addIngredient(request.POST)
    recipe.ingredients.add(ingredient)
    return redirect('/addIngr/'+id)

def show(request, id):
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'recipe': Recipe.objects.get(id = id),
    'ingredients': Ingredient.objects.filter(recipes__id = id)
    }
    return render(request, 'home/showRecipe.html', context);

def clear_recipe(request):
    request.session['curRecipe'] = ''
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name'])
    }
    return render(request, 'home/index.html', context);

def delete_Recipe(request, id):
    recipe = Recipe.objects.get(id = id)
    recipe.delete()
    return redirect('/recipes')
