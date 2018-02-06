from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)


    def __str__(self):
         return "Пользователь %s %s" % (self.name, self.email,)

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Мои заказчики'


class About(models.Model):
    title = models.CharField(max_length=68)  # заголовок поста
    content = RichTextUploadingField()  # текст поста



    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
