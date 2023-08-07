from django.db import models

# Create your models here.
class Category(models.Model):
    """Категории"""
    category = models.CharField("Категория", max_length=150)
    
    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    """Продукты"""
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    price = models.PositiveIntegerField("Цена", default=0, help_text="указывать сумму в баллах")

    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Product_images(models.Model):
    """Картинки продукта"""
    name = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Картинка продукта"
        verbose_name_plural = "Картинки продукта"


class Size(models.Model):
    """Размеры"""
    size = models.CharField("Размер", max_length=5)
    
    def __str__(self):
        return self.size
    
    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"


class Amount_of_products(models.Model):
    """Количество"""
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)
    size = models.ForeignKey(Size, verbose_name="Размер", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField("Цена", default=0, help_text="указывать количество")

    def __str__(self):
        return self.size
    
    class Meta:
        verbose_name = "Количество"
        verbose_name_plural = "Количество"

class User_products(models.Model):
    """Заказы пользователя"""
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)
    # user = models.ForeignKey(User, verbose_name="Продукт", on_delete=models.CASCADE)
    size = models.ForeignKey(Size, verbose_name="Размер", on_delete=models.CASCADE)

    def __str__(self):
        return self.size
    
    class Meta:
        verbose_name = "Заказ пользователя"
        verbose_name_plural = "Заказы пользователя"

    



