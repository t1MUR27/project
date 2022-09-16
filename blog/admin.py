from django.contrib import admin
from .models import Category, Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'is_published')
    list_display_links = ('pk', 'title')
    list_editable = ('is_published',)

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)



