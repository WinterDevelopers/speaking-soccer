from django.contrib import admin
from blog.models import Post, Comment, Subscribers
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title','status', 'created_on', 'counts',)
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')

admin.site.register(Post, PostAdmin)

admin.site.register(Subscribers)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
