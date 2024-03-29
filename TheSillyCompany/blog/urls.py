from django.conf.urls import url, include
from rest_framework import routers
from blog.quickstart import viewsAPI

from django.urls import path
from django.conf.urls import include, url
from . import views

router = routers.DefaultRouter()
router.register(r'users', viewsAPI.UserViewSet)
router.register(r'groups', viewsAPI.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API



urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('u-desk.html', views.udesk, name='u-desk'),
    path('curtain.html', views.curtain, name='curtain'),
    path('armband.html', views.armband, name='armband'),
    path('nosotros.html', views.nosotros, name='nosotros'),
    path('comunidad.html', views.comunidad, name='comunidad'),
    #login
    path('welcome.html', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    

    #path('admin/', admin.site.urls),
]


