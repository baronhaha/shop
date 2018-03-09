#coding: utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation



class Post(models.Model):

    title = models.CharField(max_length=80) # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    content = RichTextUploadingField() # текст поста
    short_content = RichTextUploadingField()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id



