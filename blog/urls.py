from django.conf.urls import url
from . import views
#from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^$', views.post_list, name='view_blogs'),
	url(r'post$',views.post_list),
	url(r'create_blog$',views.create_blog, name='create_blog'),
#	url(r'login$', auth_views.login, name='login'),
]
