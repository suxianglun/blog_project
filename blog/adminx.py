from django.contrib import admin
from blog.models import Post, Category, Tag
import xadmin


# Register your models here.
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']
#
#
# class TagAdmin(admin.ModelAdmin):
#     list_display = ['name']
#
#
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'excerpt', 'category', 'author', 'views', 'create_time', 'modified_time',
#                     'image_img']
#
#
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Tag, TagAdmin)
# admin.site.register(Post, PostAdmin)


class CategoryAdmin(object):
    list_display = ['name']


class TagAdmin(object):
    list_display = ['name']


class PostAdmin(object):
    list_display = ['title', 'excerpt', 'category', 'views', 'modified_time', 'image_img',
                    'img_url']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Post, PostAdmin)
