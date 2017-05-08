# coding: utf-8

from django import template

from ..models import Post, Category

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]


# 归档
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


# 分类
@register.simple_tag
def get_categories():
    return Category.objects.all()
