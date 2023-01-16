from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def index(request):
    return render(request,'adminindex.html')

def view_add_recipe(request):
    return render(request, 'add_recipe.html')

def add_recipe(request):
    if request.method == 'POST':
        name = request.POST['recipe_name']
        image = request.FILES['recipe_image']
        recipe_instructions = request.POST['instructions']
        recipe_ingredients = request.POST['ingredients']
    data = Recipedb(recipe_name = name, recipe_image = image, instruction = recipe_instructions, ingredients = recipe_ingredients)
    data.save()
    return redirect('view')

def view(request):
    data = Recipedb.objects.all()
    return render(request, 'view_recipe.html', {'data': data})