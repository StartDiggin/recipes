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
    url(r'^delete/(?P<id>\d+)$', views.delete_Recipe),
    url(r'^logout$', views.Logout),
    url(r'^beef$', views.beef),
    url(r'^chicken$', views.chicken),
    url(r'^seafood$', views.seafood),
    url(r'^dessert$', views.dessert),
    url(r'^pork$', views.pork),
    url(r'^sides$', views.sides),
    url(r'^pasta$', views.pasta),
    url(r'^drinks$', views.drinks),
    url(r'^deleteIngr/(?P<id>\d+)$', views.deleteIngr),
]
