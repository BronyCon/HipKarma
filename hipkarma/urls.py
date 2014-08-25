from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

import karma.views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', hipkarma.views.home, name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^karma$', karma.views.karma, name='karma'),
                       url(r'^emotes$', karma.views.emotes, name='emotes'),
                       url(r'^$', karma.views.index, name='index'),
                       url(r'^admin/', include(admin.site.urls)),
)
