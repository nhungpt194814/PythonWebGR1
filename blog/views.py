from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.forms import CommmentForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView
# generic views helps optimize your code

# Create your views here.


def post(request, pk):
    # get Post with pk=pk, if not exits return 404
    post = get_object_or_404(Post, pk=pk)
    form = CommmentForm()
    if request.method == 'POST':
        form = CommmentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'blog/post.html', {'post': post, 'form': form})


class PostListView(ListView):
    # order blog posts by date
    queryset = Post.objects.all().order_by('-date')
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 1  # maximum per page is 1 blog posts


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post.html'
