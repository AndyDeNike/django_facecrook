#this file is used to display models in django admin panel 
from django.contrib import admin
from .models import Post

admin.site.register(Post)


