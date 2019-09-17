from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.utils.text import slugify


from blog.models import Post, Category, Tag
from blog.utils.pager import PageInfo
import mistune
import markdown
from markdown.extensions.toc import TocExtension

# Create your views here.
class BaseView(View):
    post_list = Post.objects.all().order_by('-id')
    context = {'post_list': post_list}


class IndexView(BaseView):
    def get(self, request):
        base_url = request.path_info
        all_count = Post.objects.all().count()
        page_info = PageInfo(request.GET.get('page'), all_count, 10, base_url, 11)
        self.context['post_list'] = self.post_list[page_info.start():page_info.end()]
        self.context['page_info'] = page_info
        return render(request, 'home.html', context=self.context)


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
        post.body_html = mistune.markdown(post.body)
        return post

    # def get_context_data(self, **kwargs):
    #     # 覆写 get_context_data目的不仅要将post传给模板（DetailView已经帮我们做了），还要将评论及表单传给模板
    #     context = super(PostDetailView, self).get_context_data(**kwargs)
    #     form = CommentForm()
    #     comment_list = self.object.comment_set.all()
    #     context.update({
    #         'form': form,
    #         'comment_list': comment_list
    #     })
    #     return context

    def post(self, request):
        return
