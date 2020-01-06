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
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^course_list/$', views.CourseListView.as_view(), name='course_list'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.CourseView.as_view(), name='course'),
]
