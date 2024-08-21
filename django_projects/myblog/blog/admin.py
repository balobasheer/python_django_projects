from django.contrib import admin
from .models import Post,CommentPost,Profile

# Register your models here.


admin.site.register(Post)
admin.site.register(CommentPost)
admin.site.register(Profile)