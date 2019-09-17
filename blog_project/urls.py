"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf.urls.static import static

import xadmin
from .settings.base import MEDIA_ROOT
from django.conf import settings

from blog import views


urlpatterns = [
                  # url(r'^admin/', admin.site.urls),
                  url(r'^admin/', xadmin.site.urls),
                  url(r'', include('blog.urls', namespace='blog')),
                  # 加载图片使用
                  url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 增加static用于配置图片资源访问
# 只有在debug 模式下使用debug_toolbar
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns
# 全局配置404 500页面
handler404 = views.page_not_found
handler500 = views.page_error