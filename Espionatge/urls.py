from django.conf.urls import patterns, include, url
from appEspionatge import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.mainpage),
    url(r'^cases/$', views.cases, name='cases'),
    url(r'^clients/$', views.clients, name='clients'),
    url(r'^detectives/$', views.detectives, name='detectives'),
    url(r'^suspects/$', views.suspects, name='suspects'),

    url(r'^cases/(\w+)/$', views.case),
    url(r'^clients/(\w+)/$', views.client),
	url(r'^suspects/(\w+)/$', views.suspect),
    url(r'^detectives/(\w+)/$', views.detective),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
