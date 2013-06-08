from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.template import Context
from django.template import RequestContext
from django.core import serializers
from django.template.loader import get_template
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404



from appEspionatge.models import *
from appEspionatge.forms import *
from xmlUtils  import *
from jsonUtils import *

def getFormat(request):

	formatting = request.GET.get('format')	
	
	if formatting == 'xml':
		return 'xml'
	elif formatting == 'json':
		return 'json'
	else:
		return 'html'
		
		
def list_all_links(model, path, request):
	format = getFormat(request)
	
	if format == "xml":
		return xml_list_all_links(model, path, request)
	elif format == "json":
		return json_list_all_links(model, path, request)
	
	
def show_content(instance, request, path ):
	format = getFormat(request)
	
	if format == "xml": 
		return xml_show_content(instance, path, request)
	elif format == "json":
		return json_show_content(instance, path, request)
	
def userpage(request, username):
	try:
		user = User.objects.get(username=username)
		user = self.adminuser
	except:
		raise Http404('User not found.')
	
	template = get_template('userpage.html')
	variables = Context({
		'username': username
		})
	output = template.render(variables)
	return HttpResponse(output)


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/cases/")
    else:
        form = UserCreationForm()
    	return render(request, "registration/register.html", {'form': form, })
    	
    
def mainpage(request):	
	template = get_template('mainpage.html')
	variables = Context({
		'user' : request.user
		})
	output = template.render(variables)
	return HttpResponse(output)
	

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
		raise Http404('Cannot find case with ID "' + str(ID) + '"')
		
	RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

	if getFormat(request) == 'html':
		template = get_template('case.html')
		variables = RequestContext(request, {
			'user' : request.user,
			'case': case,
			'RATING_CHOICES' : RATING_CHOICES
			})
		output = template.render(variables)
	else:
		output = show_content(case, request, 'cases')
		
	return HttpResponse(output)


def update_case(request, ID):
	try:
		case = Case.objects.get(id=ID)	
	except:
		raise Http404('Cannot find case with ID "' + str(ID) + '"')

	case.name 		=	request.POST.get('name')
	case.date 		=	request.POST.get('date')
	case.clients 	=	request.POST.get('clients')
	case.suspects 	=	request.POST.get('suspects')
	case.detective 	=	request.POST.get('detective')
	case.price 		=	request.POST.get('price')
	

	case.save()

	return HttpResponse('updated')


def delete_case(request, ID):
	try:
		case = Case.objects.get(id=ID)	
	except:
		raise Http404('Cannot find case with ID "' + str(ID) + '"')

	case.delete()

	return redirect('/cases/')

@csrf_protect
def client(request, ID):
	try:
		client = Client.objects.get(id=ID)	
	except:
		raise Http404('Cannot find client with ID "' + str(ID) + '"')

	RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))


	if getFormat(request) == 'html':
		template = get_template('client.html')
		variables = RequestContext(request, {
			'user' : request.user,
			'client': client,
			'RATING_CHOICES' : RATING_CHOICES
			})
		output = template.render(variables)
	else:
		output = show_content(client, request, 'clients')
		
	return HttpResponse(output)	


def update_client(request, ID):
	try:
		client = Client.objects.get(id=ID)	
	except:
		raise Http404('Cannot find client with ID "' + str(ID) + '"')

	client.name 	=	request.POST.get('name')
	client.hide_id	=	request.POST.get('hide_id')

	client.save()

	return HttpResponse('updated')

def delete_client(request, ID):
	try:
		client = Client.objects.get(id=ID)	
	except:
		raise Http404('Cannot find client with ID "' + str(ID) + '"')

	client.delete()

	return redirect('/clients/')


def suspect(request, ID):
	try:
		suspect = Suspect.objects.get(id=ID)	
	except:
		raise Http404('Cannot find suspect with ID "' + str(ID) + '"')

	RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
	
	if getFormat(request) == 'html':
		template = get_template('suspect.html')
		variables = RequestContext(request, {
			'user' : request.user,
			'suspect': suspect,
			'RATING_CHOICES' : RATING_CHOICES
			})
		output = template.render(variables)
	else:
		output = show_content(suspect, request, 'suspects')
		
	return HttpResponse(output)	


def update_suspect(request, ID):
	try:
		suspect = Suspect.objects.get(id=ID)	
	except:
		raise Http404('Suspect not found.')

	suspect.name 	=	request.POST.get('name')
	suspect.history =	request.POST.get('history')

	suspect.save()

	return HttpResponse('updated')


def delete_suspect(request, ID):
	try:
		suspect = Suspect.objects.get(id=ID)	
	except:
		raise Http404('Cannot find suspect with ID "' + str(ID) + '"')

	suspect.delete()

	return redirect('/suspects/')
		

def detective(request, ID):
	try:
		detective = Detective.objects.get(id=ID)	
	except:
		raise Http404('Cannot find detective with ID "' + str(ID) + '"')

	if getFormat(request) == 'html':
		template = get_template('detective.html')
		variables = Context({
			'user' : request.user,
			'detective': detective
			})
		output = template.render(variables)
	else:
		output = show_content(detective, request, 'detectives')
		
	return HttpResponse(output)	


def update_detective(request, ID):
	try:
		detective = Detective.objects.get(id=ID)	
	except:
		raise Http404('Cannot find detective with ID "' + str(ID) + '"')

	detective.name =		request.POST.get('name')
	detective.rate =		request.POST.get('rate')
	detective.experience = 	request.POST.get('experience')
	detective.save()

	return HttpResponse('updated')

def delete_detective(request, ID):
	try:
		detective = Detective.objects.get(id=ID)	
	except:
		raise Http404('Cannot find detective with ID "' + str(ID) + '"')

	detective.delete()

	return redirect('/detectives/')


class CaseCreate(CreateView):
		
	model = Case
	template_name = 'form.html'
	form_class = CaseForm
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CaseCreate, self).form_valid(form)


class ClientCreate(CreateView):

	model = Client
	template_name = 'form.html'
	form_class = ClientForm
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ClientCreate, self).form_valid(form)


class SuspectCreate(CreateView):

	model = Suspect
	template_name = 'form.html'
	form_class = SuspectForm
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(SuspectCreate, self).form_valid(form)


class DetectiveCreate(CreateView):

	model = Detective
	template_name = 'form.html'
	form_class = DetectiveForm
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(DetectiveCreate, self).form_valid(form)


@csrf_protect
def create_client_review(request, pk):

	client = get_object_or_404(Client, pk=pk)
	to_redirect = '/clients/' + str(pk)
	review = ClientReview	(
								rating=request.POST['rating'],
								comment=request.POST['comment'],
								user=request.user,
								client=client
							)
	review.save()
	return redirect(to_redirect)

@csrf_protect
def create_suspect_review(request, pk):

	suspect = get_object_or_404(Suspect, pk=pk)
	to_redirect = '/suspects/' + str(pk)
	review = SuspectReview 	(
								rating=request.POST['rating'],
								comment=request.POST['comment'],
								user=request.user,
								suspect=suspect 
							)
	review.save()
	return redirect(to_redirect)

@csrf_protect
def create_case_review(request, pk):

	case = get_object_or_404(Case, pk=pk)
	to_redirect = '/cases/' + str(pk)
	review = CaseReview 	(
								rating=request.POST['rating'],
								comment=request.POST['comment'],
								user=request.user,
								case=case 
							)
	review.save()
	return redirect(to_redirect)


def getClientReviews(client):
	pass

def getSuspectReview(suspect):
	pass

def getCaseReview(case):
	pass

