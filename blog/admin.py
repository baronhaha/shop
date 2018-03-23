# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Post, PostCategory


class PostCategoryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in PostCategory._meta.fields]


    class Meta:
        model = PostCategory

admin.site.register(PostCategory, PostCategoryAdmin)


admin.site.register(Post)

