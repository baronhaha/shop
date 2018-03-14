#coding: utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation


class PostCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)


    def __str__(self):
      return "%s" % self.name


    class Meta:
       verbose_name = 'Категория поста'
       verbose_name_plural = 'Категория постов'

class Post(models.Model):

    title = models.CharField(max_length=80) # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    content = RichTextUploadingField() # текст поста
    short_content = RichTextUploadingField()
    category = models.ForeignKey(PostCategory, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id



