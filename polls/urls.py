#encoding:utf-8
from django.conf.urls import patterns,url
from polls import views
#urls文件中必须定义urlpatterns变量保存所有url映射
urlpatterns = patterns('',
    #第一个参数regex，必须的，定义URL的一个正则表达式，用于匹配请求的URL。
    #这个正则表达式不会匹配参数。Django中不需要复杂的正则表达式，性能不好。
    #第二个参数view，必须的，URL匹配后将Request作为第一个参数，其他作为其他参数传入的view中的函数。
    #该函数用于处理请求，并返回response对象
    #kwargs参数，可选的，向view中的函数传入任意的key-value
    #name参数，可选的，用于定义该映射关系的名称，用于重用
    url(r'^$',views.index,name='polls-index'),
    url(r'^(?P<poll_id>\d+)/$',views.detail,name='polls-detail'),
    url(r'^(?P<poll_id>\d+)/results/$',views.results,name='polls-results'),
    url(r'^(?P<poll_id>\d+)/vote/$',views.vote,name='polls-vote'),
)