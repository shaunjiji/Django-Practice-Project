from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def register(request):
    return HttpResponse("Hello Worlds")