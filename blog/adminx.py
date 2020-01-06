from django.contrib import admin

import xadmin
from xadmin import views
from xadmin.layout import Row, Fieldset, Container

from blog.forms.news import PostAdminForm
from blog.models import Post, Category, Tag, Course,NavMenu


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

# 同样是在adminx.py文件下
class BaseSetting(object):
    enable_themes = True  # 添加主题选择功能
    use_bootswatch = True  # 添加多个主题到选择中


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    site_title = '博客后台管理系统'
    site_footer = '尼古拉斯特仑苏'
    # menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSettings)


class NavMenuAdmin(object):
    list_display = ['name']


class CategoryAdmin(object):
    list_display = ['name']


class TagAdmin(object):
    list_display = ['name']


class CourseAdmin(object):
    list_display = ['name', 'image_img', 'url']


class PostAdmin(object):
    form = PostAdminForm
    list_display = ['title', 'category', 'author', 'create_time', 'image_img', 'url']
    form_layout = (
        Fieldset(
            '基础信息',
            Row("title", "category"),
        ),
        Fieldset(
            '内容信息',
            'is_md',
            'content_ck',
            'content_md',
            'content',
        )
    )


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(NavMenu, NavMenuAdmin)
