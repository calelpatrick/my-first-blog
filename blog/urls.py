from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.hab_list),
	url(r'^hab/(?P<pk>[0-9]+)/$', views.hab_detail),
	url(r'^hab/new/$', views.hab_new, name='hab_new'),
]