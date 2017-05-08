# coding: utf-8

# from django.http import HttpResponse
# Create your views here.
import markdown
# import markdown2
from django.shortcuts import render, get_object_or_404

from .models import Post, Category
from comments.forms import CommentForm


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # post.body = markdown2.markdown(post.body, extras=['fenced-code-blocks'],)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    # post_list = Post.objects.filter(created_time__day=14)
    # post_list = Post.objects.filter(modified_time__month=month)
    return render(request, 'blog/index.html', context={'post_list': post_list})


