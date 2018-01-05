#coding: utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin


class Post(models.Model, HitCountMixin):
    title = models.CharField(max_length=60) # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    content = RichTextUploadingField() # текст поста
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id


