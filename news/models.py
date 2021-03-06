from django.db import models
from PIL import Image
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField



class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    banner_image = models.ImageField(upload_to='media_pics/%Y/%m/%d', blank=True, default='default-banner.jpg')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=250)
    date_posted = models.DateField()
    body = RichTextUploadingField()

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def get_absolute_url(self):
        return f'news/{self.id}/{self.slug}'

    def __str__(self):
        return self.title + " " + str(self.date_posted)
