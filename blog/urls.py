from django.urls import path,re_path
from . import views


urlpatterns	=[
	path('',views.post_list, name='list'),
	re_path('^post/(?P<pk>\d+)/$',	views.post_detail,	name='post_detail'),
]