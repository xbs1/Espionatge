from django.forms import ModelForm
from appEspionatge.models import Client, Case, Suspect, Detective

class CaseForm (ModelForm):
	class Meta:
		model = Case
		exclude = ('id',)
		
class ClientForm (ModelForm):
	pass
	
class SuspectForm (ModelForm):
	pass
	
class DetectiveForm (ModelForm):
	pass
