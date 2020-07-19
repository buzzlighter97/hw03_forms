from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Post, Group
from django.shortcuts import redirect
import datetime as dt


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    posts = group.groups_posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


@login_required
def new_post(request):
    if request.method != 'POST':
        pass
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if not form.is_valid():
            pass
        elif form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        return render(request, 'new_post.html', {'form': form})
    form = PostForm()
    return render(request, 'new_post.html', {'form': form})