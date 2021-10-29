from django.contrib import admin

from . import models


class CommentInLine(admin.StackedInline):
    model = models.CommentPost

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.CommentPost)
