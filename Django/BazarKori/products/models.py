from django.db import models

# Create your models here.


class Inventory(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()

	def __str__(self):
		return self.name

class Item(models.Model):
	"""docstring for Products"""
	category 	= models.ForeignKey(Inventory, on_delete=models.CASCADE )
	title 		= models.CharField(max_length=120)
	price		= models.DecimalField(decimal_places=2, max_digits=20, default=19.99)
	image_url	= models.CharField(max_length=520, default=" ")
	featured	= models.BooleanField(default=False)

	def __str__(self):
		return self.title

