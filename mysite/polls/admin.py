from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    extra = 2
    list_display = ()

admin.site.register(Post)