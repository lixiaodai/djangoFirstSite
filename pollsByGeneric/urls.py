from django.conf.urls import url,patterns
from pollsByGeneric import views 

urlpatterns = ('',
        url(r'^$', views.IndexView.as_view(),name='pollsByG-index'),
        url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(),name='pollsByG-detail'),
        url(r'^(?P<pk>\d+)/results/$',views.ResultsView.as_view(),name='pollsByG-results'),
        url(r'^(?P<poll_id>\d+)/vote/$',views.vote,name='pollsByG-vote')
    
    )