# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ItemManager(models.Manager):
    def addItem(self, postData):
        item = Item.objects.create(name = postData['name']);
        return item;

class Item(models.Model):
    name = models.CharField(max_length=255);
    objects = ItemManager();
