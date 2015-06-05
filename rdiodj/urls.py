from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rdiodj import views

import api_views


admin.autodiscover()


urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^p/((?P<room_name>[A-Za-z0-9\-_]+)/)?$', views.party, name='party'),
    url(r'^parties/$', views.parties, name='parties'),

    url(r'^sign-out/$', logout, {'next_page': '/'}, name='sign-out'),

    url(r'^player/helper/', views.player_helper, name='player-helper'),

    url(r'^auth/', include('social_auth.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create-auth/', views.createauthtoken),

    url(r'^api/parties', api_views.parties, name='parties'),

    url(r'^api/messages/((?P<room_id>[0-9]+)/)?$', api_views.messages, name='messages'),
]


urlpatterns += staticfiles_urlpatterns()
