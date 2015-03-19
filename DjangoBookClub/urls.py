from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookit.views import Registration, Instructions, AppLogin, MainLogin, BookDump
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/$',Registration.as_view()),
    url(r'^instructions/$',Instructions.as_view()),
    url(r'^applogin/$',AppLogin.as_view()),
    url(r'^$',MainLogin.as_view()),
    url(r'^books/$',csrf_exempt(BookDump.as_view())),
)