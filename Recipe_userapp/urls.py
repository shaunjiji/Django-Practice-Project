from django.urls import path
from . import views
from django.utils.datastructures import MultiValueDictKeyError

urlpatterns = [
path('register/', views.register, name='register'),
path('register_account/', views.send_message, name='send_message')
]

