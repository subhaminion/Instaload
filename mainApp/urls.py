from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^insta/download/', views.download, name="download")
    # url(r'^(?P<album_id>[0-9]+)/$',views.details, name='')
]
