#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# @Date    : 2019-08-09
# @Author  : suxianglun
# @Describe :
# @Version :

from .base import *  # NOQA
ALLOWED_HOSTS = ['127.0.0.1', 'localhost ', '.suxianglun.com']
DEBUG = False

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
MIDDLEWARE += [
    'django_pdb.middleware.PdbMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]
ADMINS = MANAGERS = (
    ('suxianglun', 'suxianglun@163.com'),  # 你的邮件地址
)

BASE_LOG_DIR = os.path.join(BASE_DIR, "log")
if not os.path.exists(BASE_LOG_DIR):
    os.mkdir(BASE_LOG_DIR)

LOGGING = {
    'version': 1,  # 保留字
    'disable_existing_loggers': False,  # 禁用已经存在的logger实例
    # 日志文件的格式
    'formatters': {
        # 详细的日志格式
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelname)s][%(message)s]'
        },
        # 简单的日志格式
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        # 定义一个特殊的日志格式
        'collect': {
            'format': '%(message)s'
        }
    },
    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理器
    'handlers': {
        # 在终端打印
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',  #
            'formatter': 'simple'
        },
        # 默认的
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "blog_info.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 3,  # 最多备份几个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 专门用来记错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "blog_error.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 专门定义一个收集特定信息的日志
        'collect': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "blog_collect.log"),
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'collect',
            'encoding': "utf-8"
        }
    },
    'loggers': {  # 收集器
        # 默认的logger应用如下配置
        '': {
            'handlers': ['default', 'error'],  # 上线之后可以把'console'移除
            'level': 'DEBUG',
            'propagate': True,  # 向不向更高级别的logger传递
        },
        # 名为 'collect'的logger还单独处理
        'collect': {
            'handlers': ['console', 'collect'],
            'level': 'INFO',
        },
        # 名为 'error'的logger还单独处理
        'error': {
            'handlers': ['console', 'error'],
            'level': 'ERROR',
        }
    },
}
