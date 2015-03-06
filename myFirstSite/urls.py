#encoding:utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myFirstSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # 设置namespace保证每个APP不会重复
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls',namespace='polls')),
)
