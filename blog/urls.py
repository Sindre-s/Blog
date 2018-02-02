from django.conf.urls import url
from . import views
#from django.contrib.auth import views


urlpatterns = [
	url(r'^$', views.post_list, name='view_blogs'),
	url(r'post$',views.post_list),
	url(r'create_blog$',views.create_blog, name='create_blog'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
#	url(r'^accounts/login/$', views.login, name='login')
]
