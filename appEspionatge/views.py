from django.http import HttpResponse, Http404
from django.template import Context
from django.core import serializers
from django.template.loader import get_template
from django.contrib.auth.models import User

from appEspionatge.models import *
from xmlUtils  import *
from jsonUtils import *

def list_all_links(model, path, request):
	format = getFormat(request)
	
	if format == "xml":
		return xml_list_all_links(model, path, request)
	elif format == "json":
		return json_list_all_links(model, path, request)
	
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
		'user' : request.user
		})
	output = template.render(variables)
	return HttpResponse(output)

def getFormat(request):
	formatting = request.GET.get('format')	
	
	if formatting == 'xml':
		return 'xml'
	elif formatting == 'json':
		return 'json'
	else:
		return 'html'

def cases(request):
	if getFormat(request) == 'html':
		cases = Case.objects.all()
		template = get_template('cases.html')
		variables = Context({
			'user' : request.user,
			'cases' : cases
			})
		output = template.render(variables)
	else:
		output = list_all_links(Case, "cases", request)
		
	return HttpResponse(output)

def clients(request):
	if getFormat(request) == 'html':
		clients = Client.objects.all()
		template = get_template('clients.html')
		variables = Context({
			'user' : request.user,
			'clients': clients
			})
		output = template.render(variables)
	else:
		output = list_all_links(Client, "clients", request)
		
	return HttpResponse(output)

def detectives(request):
	if getFormat(request) == 'html':
		detectives = Detective.objects.all()
		template = get_template('detectives.html')
		variables = Context({
			'user' : request.user,
			'detectives': detectives
		})
		output = template.render(variables)
	else:
		output = list_all_links(Detective, "detectives", request)
	
	return HttpResponse(output)

def suspects(request):
	if getFormat(request) == 'html':
		suspects = Suspect.objects.all()
		template = get_template('suspects.html')
		variables = Context({
			'user' : request.user,
			'suspects': suspects
		})
		output = template.render(variables)
	else:
		output = list_all_links(Suspect, "suspects", request)
		
	return HttpResponse(output)

def case(request, ID):
	try:
		case = Case.objects.get(id=ID)
	except:
		raise Http404('Case not found.')
	
	template = get_template('case.html')
	variables = Context({
		'user' : request.user,
		'case': case
		})
	output = template.render(variables)
	return HttpResponse(output)

def client(request, ID):
	try:
		client = Client.objects.get(id=ID)	
	except:
		raise Http404('Client not found.')

	template = get_template('client.html')
	variables = Context({
		'user' : request.user,
		'client': client
		})
	output = template.render(variables)
	return HttpResponse(output)	

def suspect(request, ID):
	try:
		suspect = Suspect.objects.get(id=ID)	
	except:
		raise Http404('Suspect not found.')

	template = get_template('suspect.html')
	variables = Context({
		'user' : request.user,
		'suspect': suspect
		})
	output = template.render(variables)
	return HttpResponse(output)		

def detective(request, ID):
	try:
		detective = Detective.objects.get(id=ID)	
	except:
		raise Http404('Detective not found.')

	template = get_template('detective.html')
	variables = Context({
		'user' : request.user,
		'detective': detective
		})
	output = template.render(variables)
	return HttpResponse(output)		
	
