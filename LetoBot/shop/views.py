from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_products(request):
    """
    GET request
    get products
    /api/v1/product/{start}/{stop}
    """


def get_product(request):
    """
    GET request
    get certain product
    /api/v1/product/{product_id}
    """


def get_categories(request):
    """
    POST request
    get categories
    /api/v1/cat/all
    """


# def