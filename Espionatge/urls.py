from django.conf.urls import patterns, include, url
from django.utils import timezone

from rest_framework import viewsets, routers

from django.views.generic import DetailView, ListView, UpdateView
from appEspionatge import views, models
from appEspionatge.forms import *

from django.contrib.auth.models import User

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
	
class ClientViewSet(viewsets.ModelViewSet):
	model = Client
	
class SuspectViewSet(viewsets.ModelViewSet):
	model = Suspect
	
class DetectiveViewSet(viewsets.ModelViewSet):
	model = Detective
	
class CaseViewSet(viewsets.ModelViewSet):
	model = Case

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'clients',    ClientViewSet)
router.register(r'suspects',   SuspectViewSet)
router.register(r'detectives', DetectiveViewSet)
router.register(r'cases',      CaseViewSet)

urlpatterns = patterns('',
	url(r'^api/', include(router.urls)),
    url(r'^$', views.mainpage),
    
    url(r'^cases/$', views.cases),
	url(r'^clients/$', views.clients),
	url(r'^detectives/$', views.detectives),
	url(r'^suspects/$', views.suspects),
	
	url(r'^cases/create/$', views.CaseCreate.as_view(success_url="/cases/")),
	url(r'^clients/create/$', views.ClientCreate.as_view(success_url="/clients/")),
	url(r'^suspects/create/$', views.SuspectCreate.as_view(success_url="/suspects/")),
	url(r'^detectives/create/$', views.DetectiveCreate.as_view(success_url="/detectives/")),
	
	url(r'^cases/(\w+)/$', views.case),
	url(r'^clients/(\w+)/$', views.client),
	url(r'^suspects/(\w+)/$', views.suspect),
	url(r'^detectives/(\w+)/$', views.detective),
	
	url(r'^cases/(?P<pk>\d+)/edit/$',
		UpdateView.as_view(
			model = models.Case,
			template_name = 'form.html',
			form_class = CaseForm,
			success_url="/cases/")),

	url(r'^cases/(\w+)/delete/$', views.delete_case),
	url(r'^clients/(\w+)/delete/$', views.delete_client),
	url(r'^suspects/(\w+)/delete/$', views.delete_suspect),
	url(r'^detectives/(\w+)/delete/$', views.delete_detective),

	url(r'^clients/(?P<pk>\d+)/edit/$',
		UpdateView.as_view(
			model = models.Client,
			template_name = 'form.html',
			form_class = ClientForm,
			success_url="/clients/")),
		
	url(r'^suspects/(?P<pk>\d+)/edit/$',
		UpdateView.as_view(
			model = models.Suspect,
			template_name = 'form.html',
			form_class = SuspectForm,
			success_url="/suspects/")),

	url(r'^detectives/(?P<pk>\d+)/edit/$',
		UpdateView.as_view(
			model = models.Detective,
			template_name = 'form.html',
			form_class = DetectiveForm,
			success_url="/detectives/")),
		
	url(r'^register/$', views.register),
	
    # Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout'),
	
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    

	#Create a client review, ex: /clients/1/reviews/create/
	url(r'^clients/(\w+)/reviews/create/$',views.create_client_review),
	#Create a suspect review, ex: /suspects/1/reviews/create/
	url(r'^suspects/(\w+)/reviews/create/$',views.create_suspect_review),
	#Create a case review, ex: /cases/1/reviews/create/
	url(r'^cases/(\w+)/reviews/create/$',views.create_case_review),


)

