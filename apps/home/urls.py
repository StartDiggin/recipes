from django.conf.urls import url
from django.http import HttpResponse
from . import views

def test(request):
    return HttpResponse("app level")

urlpatterns = [
    url(r'^$', views.index),
    url(r'^createUser$', views.create_user),
    url(r'^login$', views.login),
    url(r'^createRecipe$', views.create_recipe),
    url(r'^recipes$', views.recipes),
    url(r'^addIngr/(?P<id>\d+)$', views.add_Ingredient),
    url(r'^addIngredient/(?P<id>\d+)$', views.add_ingre_to_recipe),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^clear$', views.clear_recipe),
    url(r'^delete/(?P<id>\d+)$', views.delete_Recipe),
]
