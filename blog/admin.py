from django.contrib import admin

from . models import Post, Category, Profile, Comment,Reply

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published']
    list_filter = ['author', 'published']
    search_fields = ['title', 'body']
    date_hierarchy = 'published'
    ordering = ['published']
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Reply)


