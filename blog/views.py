from django.shortcuts import render
from django.views import View

from blog.models import Post, Category, Tag
from blog.utils.pager import PageInfo


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
