from django.contrib import admin
from .models import Animal, Post, Photo

# Register your models here.

admin.site.register(Animal)
admin.site.register(Post)
admin.site.register(Photo)
