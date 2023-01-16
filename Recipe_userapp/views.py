from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from . models import *

# Create your views here.

def register(request):
    return render (request, 'register.html')

def send_message(request):
    if request.method == 'POST':
        user_name = request.POST['recipe']
        user_email = request.POST['email']
        user_subject = request.POST['subject']
        user_message = request.POST['message']
    data = Contactdb(name = user_name, email = user_email, subject = user_subject, message = user_message)
    data.save()
    return redirect('register')
    