from django.urls import path

from . import views

urlpatterns = [
	#/products/
    path('', views.products, name='products'),

    #/products/<product_id>/
    path('<int:item_id>/',views.detail,name='detail'),

]
