from django.contrib import admin
from .models import News

admin.site.site_header = "Research Administration"

admin.site.register(News)
