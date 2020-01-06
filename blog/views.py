from django.shortcuts import render, render_to_response
from django.views import View
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

from django.utils.text import slugify

from blog.models import Post, Category, Tag, Course,NavMenu
from blog.utils.pager import PageInfo
from django.views.decorators.csrf import csrf_exempt

import mistune
import markdown
from markdown.extensions.toc import TocExtension


# Create your views here.
# class BaseView(View):
#     post_list = Post.objects.all().order_by('-id')
#     context = {'post_list': post_list}


class IndexView(View):
    def get(self, request):
        post_list = Post.objects.all().order_by('-id')
        category_list = Category.objects.all()
        tag_list = Tag.objects.all()
        course_list = Course.objects.all()
        menu_list = NavMenu.objects.all()

        context = {'post_list': post_list, 'category_list': category_list, 'tag_list': tag_list,
                   'course_list': course_list, 'menu_list': menu_list,}

        base_url = request.path_info
        all_count = Post.objects.all().count()
        page_info = PageInfo(request.GET.get('page'), all_count, 10, base_url, 11)
        context['post_list'] = post_list[page_info.start():page_info.end()]
        context['page_info'] = page_info

        return render(request, 'home.html', context=context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog-detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(self, request, *args, **kwargs)
        self.object.increate_views()
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)

        # convert 方法将 post.body 中的 Markdown 文本渲染成 HTML 文本
        post.body_html = mistune.markdown(post.content)
        return post

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data目的不仅要将post传给模板（DetailView已经帮我们做了），还要将评论及表单传给模板
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post_list = Post.objects.all().order_by('-id')
        category_list = Category.objects.all()
        tag_list = Tag.objects.all()
        course_list = Course.objects.all()
        menu_list = NavMenu.objects.all()
        context.update({
            'post_list': post_list,
            'category_list': category_list,
            'tag_list': tag_list,
            'course_list': course_list,
            'menu_list': menu_list,
        })
        return context

    def post(self, request):
        return


class CategoryView(View):

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        post_list = Post.objects.filter(category=category).order_by('-id')
        category_list = Category.objects.all()
        tag_list = Tag.objects.all()
        course_list = Course.objects.all()
        menu_list = NavMenu.objects.all()
        context = {'post_list': post_list, 'category_list': category_list, 'tag_list': tag_list,
                   'course_list': course_list,
                   'menu_list': menu_list,}
        return render(request, 'home.html', context=context)


class TagView(View):

    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        post_list = Post.objects.filter(tag=tag).order_by('-id')
        category_list = Category.objects.all()
        tag_list = Tag.objects.all()
        course_list = Course.objects.all()
        menu_list = NavMenu.objects.all()
        context = {'post_list': post_list, 'category_list': category_list, 'tag_list': tag_list,
                   'course_list': course_list,'menu_list': menu_list,}
        return render(request, 'home.html', context=context)


class CourseListView(View):
    def get(self, request):
        post_list = Post.objects.all().order_by('-id')
        category_list = Category.objects.all()
        tag_list = Tag.objects.all()
        course_list = Course.objects.all()
        menu_list = NavMenu.objects.all()
        context = {'post_list': post_list, 'category_list': category_list, 'tag_list': tag_list,
                   'course_list': course_list,'menu_list': menu_list,}
        return render(request, 'course.html', context=context)


class CourseView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        post_list = Post.objects.filter(course=course)

        category_list = Category.objects.all()
        tag_list = Tag.objects.all()
        course_list = Course.objects.all()
        menu_list = NavMenu.objects.all()
        context = {'post_list': post_list, 'category_list': category_list, 'tag_list': tag_list,
                   'course_list': course_list,'menu_list': menu_list,}
        return render(request, 'home.html', context=context)


@csrf_exempt
def page_not_found(request):
    return render_to_response('404.html')


@csrf_exempt
def page_error(request):
    return render_to_response('500.html')
