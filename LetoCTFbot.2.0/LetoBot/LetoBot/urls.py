"""
URL configuration for LetoBot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/order/', UserProductView.as_view(),name='user_products'),
    path('api/v1/product/<int:product_id>', GetProducts.get_product ,name='product'),
    path('api/v2/product/<int:start_id>/<int:end_id>', GetProducts.get_interval ,name='product_interval'),
    path('api/v1/cat/all', GetCategories.get_categories,name='Category'),
    path('get_amounts', GetAmaunt.get_amounts,name='Количество'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)