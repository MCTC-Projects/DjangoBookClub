from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookit.views import Registration


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoBookClub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/',Registration.as_view())
)
