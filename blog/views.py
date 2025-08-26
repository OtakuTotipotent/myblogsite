from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, PostSearchForm


# home = index = post_list
def home(request):
    posts = Post.objects.all().order_by("-created_at")
    form = PostSearchForm(request.GET or None)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        start_date = form.cleaned_data.get("start_date")
        end_date = form.cleaned_data.get("end_date")
        if title:
            posts = posts.filter(title__icontains=title)
        if start_date:
            posts = posts.filter(created_at__date__gte=start_date)
        if end_date:
            posts = posts.filter(created_at__date__lte=end_date)
    return render(request, "blog/home.html", {"posts": posts, "form": form})


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
