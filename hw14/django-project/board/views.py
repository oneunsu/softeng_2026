from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
        'no_category_post_count': Post.objects.filter(category=None).count(),
    }

    return render(request, 'board/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = Category.objects.all()

    context = {
        'post': post,
        'categories': categories,
        'no_category_post_count': Post.objects.filter(category=None).count(),
    }

    return render(request, 'board/post_detail.html', context)