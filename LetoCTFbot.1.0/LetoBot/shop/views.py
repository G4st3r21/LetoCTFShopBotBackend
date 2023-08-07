from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product, Product_images, User_products, Amount_of_products, Category
from django.db import models


# Create your views here.
class GetProducts:
	"""Запросы к товарам"""

	def get_product(request):
		"""
		GET request; get certain product; /api/v1/product/{product_id};
		"""


	def get_products(request):
		"""
		GET request; get products; /api/v1/product/{start}/{stop}
		"""
		model = Product
		products = Product.objects.all()
		data = [
			{'name': product.name}
			for product in products
		]
		return JsonResponse(data, safe=False)


def get_categories(request):
	"""
	POST request
	get categories
	/api/v1/cat/all
	"""


# def