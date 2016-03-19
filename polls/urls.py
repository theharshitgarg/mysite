from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    #url(r'^$', views.home, name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    #url(r'^line/', views.vote, name='vote'),
    url(r'^line/$', views.line, name='line'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^home/$', views.home, name='home'),

)