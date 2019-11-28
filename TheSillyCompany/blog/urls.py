from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('u-desk.html', views.udesk, name='u-desk'),
    path('curtain.html', views.curtain, name='curtain'),
    path('armband.html', views.armband, name='armband'),
    path('nosotros.html', views.nosotros, name='nosotros'),
    path('comunidad.html', views.comunidad, name='comunidad'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit')
]
