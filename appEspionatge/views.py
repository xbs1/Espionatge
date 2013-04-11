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
	clients = Client.objects.all()
	template = get_template('clients.html')
	variables = Context({
		'clients': clients
		})
	output = template.render(variables)
	return HttpResponse(output)

def detectives(request):
	detectives = Detective.objects.all()
	template = get_template('detectives.html')
	variables = Context({
		'detectives': detectives
	})
	output = template.render(variables)
	return HttpResponse(output)

def suspects(request):
	suspects = Suspect.objects.all()
	template = get_template('suspects.html')
	variables = Context({
		'suspects': suspects
	})
	output = template.render(variables)
	return HttpResponse(output)

def case(request, ID):
	try:
		case = Case.objects.get(id=ID)
	except:
		raise Http404('Case not found.')
	
	template = get_template('case.html')
	variables = Context({
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
		'detective': detective
		})
	output = template.render(variables)
	return HttpResponse(output)		
