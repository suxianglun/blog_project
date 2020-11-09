from django.db import models
from datetime import datetime

# Create your models here.
from django.utils.six import python_2_unicode_compatible
from django.conf import settings
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse
from django.utils.html import strip_tags

from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID

import markdown
import mistune

import pdb


class Course(models.Model):
    """
    教程
    """
    name = models.CharField(verbose_name='名称', max_length=30)
    # 配图
    image = StdImageField(verbose_name='配图', blank=True,
                          upload_to=UploadToUUID(path='images'),  # 上传路径并使用uuid重新命名 MEDIA_ROOT/images/#UUID#.#EXT#
                          variations={'thumbnail': {"width": 200, "height": 200, "crop": True}})  # 缩略图

    @python_2_unicode_compatible
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = '教程'

    def url(self):
        """
        获取img_url
        :return:
        """
        if self.image:
            return self.image.url
        else:
            return "url为空"

    def image_img(self):
        if self.image:
            href = self.image.url  # 点击后显示的放大图片
            src = self.image.thumbnail.url  # 页面显示的缩略图
            # 插入html代码
            image_html = '<a href="%s" target="_blank" title="图片下载地址"><img alt="" src="%s"/>' % (href, src)
            return image_html
        else:
            return '上传图片'

    image_img.short_description = '显示图片'  # 显示在页面的内容
    image_img.allow_tags = True  # True 显示图片 False显示html代码


class NavMenu(models.Model):
    """
    导航栏菜单
    """
    name = models.CharField(verbose_name='名称', max_length=60)

    @python_2_unicode_compatible
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = '导航栏菜单'


class Category(models.Model):
    """
    分类
    """
    name = models.CharField(verbose_name='名称', max_length=100)
    nav_menu = models.ForeignKey(NavMenu, verbose_name='导航栏菜单')

    @python_2_unicode_compatible
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = '分类'


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(verbose_name='名称', max_length=100)

    @python_2_unicode_compatible
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = '标签'


# Create your models here.
class Post(models.Model):
    class Meta:
        '''
        News 类的内部定义一个 Meta 类，并指定排序属性：
        ordering 属性用来指定文章排序方式，['-created_time'] 指定了依据哪个属性的值进行排序，这里指定为按照文章发布时间排序，
        且负号表示逆序排列。列表中可以用多个项，比如 ordering = ['-created_time', 'title'] ，
        那么首先依据 created_time 排序，如果 created_time 相同，则再依据 title 排序。
        '''
        ordering = ['-create_time']

        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        # db_table = "table_name"

        # admin中显示的表名称
        verbose_name = '文章'

        # verbose_name加s
        verbose_name_plural = '文章'

    # 文章标题
    title = models.CharField(verbose_name='标题', max_length=100)
    # 根据喜好选择admin编辑器：富文本和Markdown
    is_md = models.BooleanField(verbose_name='markdown语法', default=False)
    content = models.TextField(verbose_name='内容')
    content_html = models.TextField(verbose_name='正文Html代码', blank=True, editable=False)

    # 创建时间
    create_time = models.DateField(verbose_name='创建时间', default=datetime.now)
    # 最后一次修改时间
    modified_time = models.DateField(verbose_name='修改时间')

    # 配图
    image = StdImageField(verbose_name='图片', blank=True,null=True,
                          upload_to=UploadToUUID(path='images'),  # 上传路径并使用uuid重新命名 MEDIA_ROOT/images/#UUID#.#EXT#
                          variations={'thumbnail': {"width": 200, "height": 200, "crop": True}})  # 缩略图

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(verbose_name='文摘', max_length=200, blank=False)

    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    # 分类 根据需求 一对多关系：一篇文章对应一个分类，一个分类有多个文章
    category = models.ForeignKey(Category, verbose_name='分类')
    # 标签  根据需求 多对多关系： 一篇文章有多个标签，一个标签有多个文章
    tag = models.ManyToManyField(Tag, verbose_name='标签', blank=True, null=True)
    # 作者
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者')

    # 教程
    course = models.ForeignKey(Course, verbose_name='教程', blank=True, null=True)

    # 阅读量 PositiveIntegerField 类型只允许其值大于等于0
    views = models.PositiveIntegerField(verbose_name='阅读量', default=0)
    # 图片已经上传情况下，直接使用img_url
    img_url = models.URLField(verbose_name='外部图片url', blank=True, null=True)

    def url(self):
        """
        获取img_url
        :return:
        """
        if self.image:
            return self.image.url
        else:
            return ""

    def image_img(self):
        if self.image:
            href = self.image.url  # 点击后显示的放大图片
            src = self.image.thumbnail.url  # 页面显示的缩略图
            # 插入html代码
            image_html = '<a href="%s" target="_blank" title="图片下载地址"><img alt="" src="%s"/>' % (href, src)
            return image_html
        else:
            return ''

    image_img.short_description = '显示图片'  # 显示在页面的内容
    image_img.allow_tags = True  # True 显示图片  False显示html代码

    def save(self, *args, **kwargs):
        """
        将Markdown转为html
        :param args:
        :param kwargs:
        :return:
        """
        if self.is_md:
            self.content_html = mistune.markdown(self.content)
        else:
            self.content_html = self.content
        super().save(*args, **kwargs)

    def increate_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    @python_2_unicode_compatible
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})
