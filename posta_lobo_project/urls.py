from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'posta_lobo_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^users/', RedirectView.as_view(url='/')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^', include('posta.urls')),

    )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root':settings.MEDIA_ROOT}),)
