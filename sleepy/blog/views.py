from django.views.generic import DetailView, ListView
from models import Post


class BlogIndex(ListView):
    model = Post
    queryset = Post.objects.published()
    template_name = 'base_blogindex.html'
    # paginate_by = 4


class BlogDetail(DetailView):
    model = Post
    template_name = 'base_blogdetail.html'
