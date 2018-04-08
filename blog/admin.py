# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Post, Category


class CategoryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]


    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


admin.site.register(Post)

