#coding: utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from django.contrib.sitemaps import Sitemap
from django.contrib.contenttypes.fields import GenericRelation
from django.core.paginator import Paginator


class Category(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    slug = models.SlugField(verbose_name='Транслит', null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products_image/')

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return "/blog/category/%i/" % self.id

    class Meta:
        db_table = 'category'
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'




class Post(models.Model):

    title = models.CharField(max_length=80) # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    content = RichTextUploadingField() # текст поста
    short_content = RichTextUploadingField()
    category = models.ForeignKey(Category, verbose_name='Категория', blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'



    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id



class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.all()

