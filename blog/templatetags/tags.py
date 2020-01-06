#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# @Date    : 2019-12-27
# @Author  : suxianglun
# @Describe :
# @Version : 
from django import template
from blog.models import Category

register = template.Library()


@register.simple_tag(name='get_category_from_menu')
def get_category_from_menu(menu_name):
    """
    博客首页获取菜单下的分类列表
    :param menu_name:
    :return:
    """
    category_list = Category.objects.filter(nav_menu__name=menu_name)
    return category_list
