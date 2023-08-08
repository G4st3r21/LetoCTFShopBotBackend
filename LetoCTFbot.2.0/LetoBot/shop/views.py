from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product, Product_images, User_products, Amount_of_products, Category
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, ProductSerializer
from .models import User, Product
import json


# Create your views here.
class GetProducts:
	"""Запросы к товарам"""

	def get_product(request, product_id):
		"""
		Выводит 1 продукт
		GET request; get certain product; /api/v1/product/{product_id};
		"""
		try:
			product = Product.objects.get(id=product_id)
			
			data = {
				'name': product.name,
				'description': product.description,
				'price': product.price,
				'category': product.category.category,
			}
			return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
		except Product.DoesNotExist:
			return JsonResponse({'error': 'Product not found'})


	def get_interval(request, start_id, end_id):
		"""
		GET request; get certain product; /api/v1/product/{product_id};
		Выводит продукты по ID в определенном интервале
		
		"""
		products = Product.objects.filter(id__range=(start_id, end_id)).values("id", "name")
		return JsonResponse(list(products), safe=False, json_dumps_params={'ensure_ascii': False})


	def get_products(request):
		"""
		GET request; get certain product; /api/v1/product/{product_id};
		Выводит все товары
		"""
		products = Product.objects.all()
		data = [{
				'name': product.name,
				'description': product.description,
				'price': product.price,
				'category': product.category.name,
				}
			for product in products
		]
		
		return JsonResponse(data, safe=False)


class GetCategories:
	def get_categories(request):
		"""
		POST request
		get categories
		/api/v1/cat/all
		выводит все категории
		"""
		
		categories = Category.objects.all()
		data = [
			{'name': category.category}
			for category in categories
		]
		return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


class GetAmaunt:
	def get_amounts(request):
		"""Выдвает количество всех товаров"""
		amounts = Amount_of_products.objects.values("product", "size", "amount")
		return JsonResponse(list(amounts), safe=False)
	
		
	
	def get_amount(request, product_id, size):
		"""Выдвает количество указанного товара"""
		try:
			product = Product.objects.get(id=product_id)
			amount_of_product = Amount_of_products.objects.get(product=product, size=size)
			data = {
				'product_id': product_id,
				'size': size,
				'amount': amount_of_product.amount
			}
			return JsonResponse(json.dumps(data), ensure_ascii=False)
		except (Product.DoesNotExist, Amount_of_products.DoesNotExist):
			return JsonResponse({'error': 'Product or Amount_of_products does not exist'})


class UserProductView(APIView):
    def get(self, request):
        users = User.objects.all()
        products = Product.objects.all()

        user_serializer = UserSerializer(users, many=True)
        product_serializer = ProductSerializer(products, many=True)

        response_data = {
            'users': user_serializer.data,
            'products': product_serializer.data
        }
        return Response(response_data)


