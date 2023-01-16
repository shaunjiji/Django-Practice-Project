from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"adminindex.html")

def view_add_recipe(request):
    return render(request, "add_recipe.html")
