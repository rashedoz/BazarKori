from django.test import TestCase
import unittest
from products.models import Item,Inventory


# Create your tests here.

class ItemTest(TestCase):
	"""Test Case for checking object craetion  Error creating Inventory Instance As Foreign Key"""
	def setUp(self):
		Inventory.objects.create(name="Fruit")
		Item.objects.create(title="Gauva",price=20,category="Fruit")
		Item.objects.create(title="Alu",price=15,category="Fruit")


	def test_item_created(self):
		Gauva =Item.objects.get(title="Gauva")
		
		Alu   =Item.objects.get(title="Alu")
		self.assertEqual(20,20)

