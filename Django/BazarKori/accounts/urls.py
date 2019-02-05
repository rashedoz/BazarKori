from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns=[
	# /accounts/

	path('signup/',views.signup.as_view(),name='signup'),


]
