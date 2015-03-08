from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookit.views import Registration,Instructions,AppLogin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/$',Registration.as_view()),
    url(r'^instructions/$',Instructions.as_view()),
    url(r'^applogin/$',AppLogin.as_view()),
)
