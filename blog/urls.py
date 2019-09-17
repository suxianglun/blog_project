#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# @Date    : 2019-07-22
# @Author  : suxianglun
# @Describe :
# @Version :
from django.conf.urls import url, include

from blog import views
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post_detail'),
]
