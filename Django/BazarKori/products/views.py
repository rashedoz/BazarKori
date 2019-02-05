from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Item, Inventory


# Create your views here.

def products(request):
	all_products = Item.objects.all()

	return render(request, 'products.html',{'all_products': all_products,})

def detail(request,item_id):
	item= get_object_or_404(Item, pk=item_id)

	return render(request , 'details.html',{'item':item})

