from django.contrib import admin
from .models import News, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('News Description', {'fields': ['title', 'description', 'image']}),
        ('Moderated', {'fields': ['moderated']}),
        ('Author', {'fields': ['author']})
    ]

    inlines = [CommentInline]

    list_display = ('title', 'author', 'moderated')
