from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nosi_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^levels/', include('levels.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
