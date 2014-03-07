from django.conf.urls import patterns, url
from posta import views

urlpatterns = patterns(' ',
    url(r'^$', views.index, name='posta.index'),
    url(r'^about/', views.about, name='posta.about'),
    url(r'^schedule/', views.schedule, name='posta.schedule'),
    url(r'^mail/$', views.mail, name='posta.mail'),
    url(r'^mail/create/$', views.mail_create, name='posta.mail.create'),
    url(r'^mail/edit/(?P<mail_url>\w+)/$', views.mail_create, name='posta.mail.edit')
)