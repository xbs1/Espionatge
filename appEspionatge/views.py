from django.http import HttpResponse, Http404

from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User

from appEspionatge.models import *

def userpage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')
	
	template = get_template('userpage.html')
	variables = Context({
		'username': username
		})
	output = template.render(variables)
	return HttpResponse(output)

def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'titlehead',
		'pagetitle': 'pagetitle',
		'contentbody': 'contentbody'
		})
	output = template.render(variables)
	return HttpResponse(output)

def cases(request):
	cases = Case.objects.all()

	template = get_template('cases.html')
	variables = Context({
		'cases' : cases
		})
	output = template.render(variables)
	return HttpResponse(output)

def clients(request):
	template = get_template('clients.html')
	variables = Context({})
	output = template.render(variables)
	return HttpResponse(output)

def detectives(request):
	template = get_template('detectives.html')
	variables = Context({})
	output = template.render(variables)
	return HttpResponse(output)

def suspects(request):
	template = get_template('suspects.html')
	variables = Context({})
	output = template.render(variables)
	return HttpResponse(output)
	
