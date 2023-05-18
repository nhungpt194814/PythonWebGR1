from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']  # show title and date
    list_filter = ['date']  # create filter with date
    search_fields = ['title']  # search with title
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)
# show these classes at admin site
