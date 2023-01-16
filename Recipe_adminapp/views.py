from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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

def admin_login(request):
    return render(request,'login.html')

def ad_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username_a'] = username
            request.session['password_a'] = password
            return redirect('login')
        else:
            return render(request,'admin_login.html', {'msg':'Sorry Invalid User Credentials'}) 
    else:
        return redirect('login')


def ad_logout(request):
    del request.session['username_a']
    del request.session['password_a']


