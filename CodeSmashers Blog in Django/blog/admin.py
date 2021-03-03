# from django.contrib import admin

# # Register your models here.
# from blog.models import Post

# # Register your models here.
# admin.site.register(Post)

from django.contrib import admin
from blog.models import Post, BlogComment

admin.site.register((BlogComment))
# admin.site.register((Post, BlogComment))





# for tiny text editor
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)