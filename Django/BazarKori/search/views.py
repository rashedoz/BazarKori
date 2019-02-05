from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from products.models import Item
from django.db import models
# Create your views here.




#Seearch function with django built in seacrh feature
def search_result(request):
	
	#Search can be changed here
	search=Item.objects.filter(title__icontains='Ba')
	#query for all products
	#search = Item.objects.all()

	return render(request, 'search.html',{'search': search,})

