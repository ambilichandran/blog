from django.contrib import admin
from.models import Post
class Addpost(admin.ModelAdmin):
    list_display=['title','image','content']
admin.site.register(Post,Addpost)
