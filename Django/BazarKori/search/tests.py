from django.test import TestCase
import unittest
from products.models import Item
# Create your tests here.




class SearchTest(unittest.TestCase):

	def test_basic(self):
		a = 1
		self.assertEqual(1,a)
