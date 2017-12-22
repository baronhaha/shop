from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255) # заголовок поста
    datetime = models.DateTimeField('Дата публикации') # дата публикации
    content = models.TextField(max_length=10000) # текст поста

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

    def save(self, *args, **kwargs):

        self.title = title
        print(self.title)



        super(Post, self).save(*args, **kwargs)
