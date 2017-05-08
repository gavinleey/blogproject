
# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['text','post',  'name', 'email', 'url' ]

admin.site.register(Comment, CommentAdmin)
