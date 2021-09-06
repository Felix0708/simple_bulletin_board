from articles.models import Article
from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'user',)


# admin site에 register 하겠다.
admin.site.register(Article, ArticleAdmin)