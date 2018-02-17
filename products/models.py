from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)


    def __str__(self):
      return "%s" % self.name


    class Meta:
       verbose_name = 'Категория товара'
       verbose_name_plural = 'Категория товаров'

class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price*nmb
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = RichTextUploadingField(blank=True, null=True, default=None)
    answer = RichTextUploadingField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)



    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
         return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


# Модель обратной связи
class Contact(models.Model):
    class Meta():
        db_table = 'contact'
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    name = models.CharField("Имя", max_length=30)
    second_name = models.CharField("Фамилия", max_length=30)
    email = models.EmailField(max_length=70)
    message = models.TextField("Сообщение", max_length=1000)
    data = models.DateTimeField("Дата отправки", default=timezone.now)

    def __str__(self):
        return self.name
