#from django.shortcuts import render,redirect
#from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

class signup(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name= 'signup.html'
