from django.shortcuts import render
from django.views import generic
from .models import Blog, BlogAuthor, BlogComment
from django.contrib.auth.models import User


def index(request):
    """
    首頁看有哪些功能
    """
    return render(
    	request,
    	'index.html',
    )
    
    
    # ListView:用來呈現資料列表的
class BlogListView(generic.ListView):
	"""
	文章列表
	"""
	model = Blog
	paginate_by = 5

from django.shortcuts import get_object_or_404


class BlogListbyAuthorView(generic.ListView):
	"""
	po文列表（po文者視圖）
	"""
	model = Blog
	paginate_by = 5
	template_name = 'blog/blog_list_by_author.html'
	
	def get_queryset(self):
	    """
	    依照po文者列表
	    """
	    id = self.kwargs['pk']
	    target_author=get_object_or_404(BlogAuthor, pk=id)
	    return Blog.objects.filter(author=target_author)
	    
	def get_context_data(self, **kwargs):
	    """
	    在內容中增加作者以展示在模板中
	    """
	    # 取得文章內容
	    context = super(BlogListbyAuthorView, self).get_context_data(**kwargs)
	    # 依pk取得po文者物件並加到內容中
	    context['blogger'] = get_object_or_404(BlogAuthor, pk = self.kwargs['pk'])
	    return context

class BlogDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = Blog

    
class BloggerListView(generic.ListView):
    """
    Generic class-based view for a list of bloggers.
    """
    model = BlogAuthor
    paginate_by = 5
