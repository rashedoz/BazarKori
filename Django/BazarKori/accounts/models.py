from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator


# Create your models here.

class Admin(User):
	username_validator = ASCIIUsernameValidator()

class Worker(User):
	"""docstring for ClassName"""


class Customer(User):
	"""docstring for Customer"""
	
		