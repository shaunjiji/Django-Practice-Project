from django.urls import path
from . import views

urlpatterns = [
path('index/', views.index, name="index"),
path('view_add_recipe/', views.view_add_recipe, name="view_add_recipe")
]

