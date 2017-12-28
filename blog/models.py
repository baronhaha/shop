#coding: utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=60) # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    content = RichTextUploadingField() # текст поста

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id


