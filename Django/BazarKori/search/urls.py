from django.urls import path

from . import views

urlpatterns = [
	#/searchPage/
    path('', views.search_result, name='search_result'),

]
