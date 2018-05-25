# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, Recipe, Ingredient

# Create your views here.
def index(request):
    if 'first_name' not in request.session:
        return render(request, 'home/index.html');
    context = {
    'curUser' : User.objects.get(first_name = request.session['first_name'])
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
    if 'first_name' not in request.session:
        messages.error(request, 'Please Login')
        return redirect('/');
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
    if 'first_name' not in request.session:
        messages.error(request, 'Please Login')
        return redirect('/');
    if 'title' not in request.session:
        context = {
        'curUser': User.objects.get(first_name = request.session['first_name']),
        'recipes': Recipe.objects.all(),
        }
        return render(request, 'home/recipePage.html', context);
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
    'curRecipe': Recipe.objects.get(id = id),
    'allIngredients': Ingredient.objects.filter(recipes__id=id),
    }
    return render(request, 'home/addIngredients.html', context);

def add_ingre_to_recipe(request, id):
    recipe = Recipe.objects.get(id = id)
    ingredient = Ingredient.objects.addIngredient(request.POST)
    recipe.ingredients.add(ingredient)
    return redirect('/addIngr/'+id)

def deleteIngr(request, id):
    recipe_id = request.session['_id']
    ingredient = Ingredient.objects.get(id = id)
    ingredient.delete()
    return redirect('/addIngr/' + recipe_id)

def show(request, id):
    request.session['_id'] = id;
    print request.session['_id']
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'recipe': Recipe.objects.get(id = id),
    'allIngredients': Ingredient.objects.filter(recipes__id=id),
    }
    return render(request, 'home/showRecipe.html', context);

def delete_Recipe(request, id):
    recipe = Recipe.objects.get(id = id)
    recipe.delete()
    return redirect('/recipes');


# Category pages
def beef(request):
    if 'first_name' not in request.session:
        messages.error(request, 'Please Login')
        return redirect('/');
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'beefRecipes': Recipe.objects.filter(amt = 'beef')
    }
    return render(request, 'home/beef.html', context)

def chicken(request):
    if 'first_name' not in request.session:
        messages.error(request, 'Please Login')
        return redirect('/');
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'chickenRecipes': Recipe.objects.filter(amt = 'chicken')
    }
    return render(request, 'home/chicken.html', context)

def pork(request):
    if 'first_name' not in request.session:
        messages.error(request, 'Please Login')
        return redirect('/');
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'porkRecipes': Recipe.objects.filter(amt = 'pork')
    }
    return render(request, 'home/pork.html', context)

def seafood(request):
    if 'first_name' not in request.session:
        messages.error(request, 'Please Login')
        return redirect('/');
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'seafoodRecipes': Recipe.objects.filter(amt = 'seafood')
    }
    return render(request, 'home/seafood.html', context)

def dessert(request):
    if 'first_name' not in request.session:
        messages.error(request, 'Please Login')
        return redirect('/');
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'dessertRecipes': Recipe.objects.filter(amt = 'dessert')
    }
    return render(request, 'home/dessert.html', context)

def sides(request):
    if 'first_name' not in request.session:
        messages.error(request, 'Please Login')
        return redirect('/');
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'sidesRecipes': Recipe.objects.filter(amt = 'sides')
    }
    return render(request, 'home/sides.html', context)

def pasta(request):
    if 'first_name' not in request.session:
        messages.error(request, 'Please Login')
        return redirect('/');
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'pastaRecipes': Recipe.objects.filter(amt = 'pasta')
    }
    return render(request, 'home/pasta.html', context)

def drinks(request):
    if 'first_name' not in request.session:
        messages.error(request, 'Please Login')
        return redirect('/');
    context = {
    'curUser': User.objects.get(first_name = request.session['first_name']),
    'drinkRecipes': Recipe.objects.filter(amt = 'drinks')
    }
    return render(request, 'home/drinks.html', context)

def Logout(request):
    request.session.flush();
    return redirect('/');
