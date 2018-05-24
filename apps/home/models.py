# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def loginVal(self, postData):
        results = {'status': True, 'errors':[], 'user': None}
        users = self.filter(first_name = postData['first_name'])

        if len(users) < 1:
            results['status'] = False
        else:
            results['user'] = users[0]

        return results

    def addUser(self, postData):
        user = User.objects.create(first_name = postData['first_name']);
        return user;

class RecipeManager(models.Manager):
    def addRecipe(self, user, postData):
        recipe_owner = User.objects.get(first_name = user)
        recipe = Recipe.objects.create(user = recipe_owner, title=postData['title'], desc=postData['desc'], inst=postData['inst'], amt=postData['amt']);
        return recipe;

class IngredientManager(models.Manager):
    def addIngredient(self, postData):
        ingredient = Ingredient.objects.create(name=postData['name']);
        return ingredient;



class User(models.Model):
    first_name = models.CharField(max_length=255);
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);
    objects = UserManager();

class Recipe(models.Model):
    title = models.CharField(max_length=255);
    desc = models.CharField(max_length=255);
    inst = models.TextField();
    amt = models.CharField(max_length=255);
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);
    user = models.ForeignKey(User, related_name="recipes");
    objects = RecipeManager();

class Ingredient(models.Model):
    name = models.CharField(max_length=255);
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);
    recipes = models.ManyToManyField(Recipe, related_name="ingredients")
    objects = IngredientManager();
