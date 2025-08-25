from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
# from django.db.models import Q

# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, "blog/home.html", {"posts": posts})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()

    return render(request, "blog/create_post.html", {"form": form})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm(instance=post)
    return render(request, "blog/edit_post.html", {"form": form})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, "blog/delete_post.html", {"post": post})
