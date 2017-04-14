from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.edit, name='add'),
    url(r'^edit/(\d+)/$', views.edit, name='edit'),
    url(r'^delete_post/(\d+)/$', views.delete_post, name='delete')
]