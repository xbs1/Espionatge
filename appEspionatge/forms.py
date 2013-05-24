from django.forms import ModelForm
from appEspionatge.models import Client, Case, Suspect, Detective

class CaseForm (ModelForm):
	class Meta:
		model = Case
		exclude = ('id',)
		
class ClientForm (ModelForm):
	class Meta:
		model = Client
		exclude = ('id',)
	
class SuspectForm (ModelForm):
	class Meta:
		model = Suspect
		exclude = ('id',)	

class DetectiveForm (ModelForm):
	class Meta:
		model = Detective
		exclude = ('id',)