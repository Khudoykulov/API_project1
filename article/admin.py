from django.contrib import admin


from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'created_date')
    list_display_links = ('id', 'author', 'title', 'created_date')
