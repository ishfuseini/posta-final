from django.conf.urls import patterns, url
from posta import views

urlpatterns = patterns(' ',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^schedule/', views.schedule, name='schedule'),
    url(r'^mail/', views.mail, name='mail'),
    url(r'^accounts/',include('registration.backends.simple.urls'),)
