from django.contrib import admin
from blog.models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,	{'fields': ['name']}),
        (None,	{'fields': ['text']}),
        ('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
    ]
    list_display=('id','name','pub_date') #显示选项
    list_filter=['name'] # 侧边栏
admin.site.register(Article, ArticleAdmin)

