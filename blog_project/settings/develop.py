#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# @Date    : 2019-07-30
# @Author  : suxianglun
# @Describe :
# @Version : 

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_project',
        'USER': 'root',
        'PASSWORD': 'qwer1234',
        'HOST': 'localhost',
        'POST': '3306',
    }
}
INSTALLED_APPS = [
    'django_pdb',  # 调试工具
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'xadmin',  # xadmin
    'crispy_forms',  # xadmin
    'reversion',
    'stdimage',  # xadmin缩略图,
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器图片上传
    'debug_toolbar',  # 调试工具
]
MIDDLEWARE += [
    'django_pdb.middleware.PdbMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]
ALLOWED_HOSTS = ['*']
DEBUG = True
