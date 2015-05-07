from django.contrib import admin
from blog.models import Article

# Register your models here.

# admin.site.register(Article) 替换为下面的：


class ArticleAdmin(admin.ModelAdmin):
    field = [
        (None, {'field': ['name']}),
        ('Date information', {'field': ['pub_date'], 'classes':['collapse']}),
    ]
    list_display = ('name', 'pub_date')
    list_filter = ['name'] #筛选
admin.site.register(Article, ArticleAdmin)
