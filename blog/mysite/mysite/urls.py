from django.conf.urls import patterns, include, url
from django.conf import settings
settings.configure()
from django.contrib import admin
import django
django.setup()
import sys
sys.path.append('../')

admin.autodiscover()
# include('blog.urls',namespace='blog')
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       url(r'^$', 'blog.views.index', name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
