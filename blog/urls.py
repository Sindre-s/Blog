from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^$', views.post_list, name='view_blogs'),
	#url(r'post$',views.post_list),
	#url(r'create_blog$',views.create_blog, name='create_blog'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^signup/$', views.signup, name='signup')
]
