#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# @Date    : 2019-07-22
# @Author  : suxianglun
# @Describe :
# @Version :
from django.conf.urls import url, include


from blog.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
]
