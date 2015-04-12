from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # http://localhost/hello/
    url(r'^hello/$', 'trips.views.hello_world'),
    # add home's url
    url(r'^$', 'trips.views.home'),

    url(r'^post/(?P<id>\d+)/$', 'trips.views.post_detail',
        name='post_detail'),
    url(r'^accounts/', include('accounts.urls')),# ADD THIS NEW TUPLE!
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)