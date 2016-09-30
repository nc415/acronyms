from django.conf.urls import url
from lists import views


urlpatterns =[
	url(r'^$', views.index, name='index'),
	#url(r'^/(?P<university_name_slug>[\w\-]+)/$', views.show_university, name='show_university'),
	]