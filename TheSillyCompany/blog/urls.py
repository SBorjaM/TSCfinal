from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('u-desk.html', views.udesk, name='u-desk'),
    path('curtain.html', views.curtain, name='curtain'),
    path('armband.html', views.armband, name='armband'),
    path('nosotros.html', views.nosotros, name='nosotros'),
    path('comunidad.html', views.comunidad, name='comunidad')
]
