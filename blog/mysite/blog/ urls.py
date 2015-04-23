from django.conf.urls import patterns, url
import sys
sys.path.append('../')
from blog import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index')
                       )
