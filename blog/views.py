from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.forms import CommmentForm, PostForm
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


def blog_post(request):
    new_post = PostForm()
    if request.method == "POST":
        new_post = PostForm(request.POST, author=request.user)
        if new_post.is_valid():
            new_post.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'blog/post.html', {'post': post, 'form': new_post})


class PostListView(ListView):
    # order blog posts by date
    queryset = Post.objects.all().order_by('-date')
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 10  # maximum per page is 1 blog posts


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post.html'
