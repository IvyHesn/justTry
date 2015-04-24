from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
'''
urlpatterns = [
    # Examples:
    # url(r'^$', 'blog_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
'''
urlpatterns = patterns('',
                       url(r'^article/(\d+)/$', 'blog.views.article', name='article'),
                       #url(r'^$', 'blog.views.index', name='index'),
                       url(r'^admin/',include(admin.site.urls)),
                       )
