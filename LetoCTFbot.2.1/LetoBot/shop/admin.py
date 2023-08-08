from django.contrib import admin
from .models import Category, Product, Product_images, Size, Amount_of_products, User_products

from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
# admin.site.register(Product_images)
admin.site.register(Size)
admin.site.register(Amount_of_products)
admin.site.register(User_products)

@admin.register(Product_images)
class ProductImagesAdmin(admin.ModelAdmin):
    """Фото продукта"""
    list_display = ("name", "product", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"