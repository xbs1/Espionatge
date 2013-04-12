from django.db import models

class Client(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=100)
	hide_id = models.BooleanField(default=False)

	def get_path(self, request):
		path = "http://" +  request.get_host() + "/clients/" + str(self.id)
		return path

	def show_content(self, path, request):
		return { 
		'id': self.id,
		'name': self.name,
		'hide_id': self.hide_id
		} 
	
	def __unicode__(self):
		return self.name		
	
class Suspect(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=100)
	history = models.TextField(max_length=200)

	def get_path(self, request):
		path = "http://" +  request.get_host() + "/suspects/" + str(self.id)
		return path		
	
	def show_content(self, path, request):
		return { 
		'id': self.id,
		'name': self.name,
		'history': self.history
		} 
		
	def __unicode__(self):
		return self.name

class Detective(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=100)
	rate = models.IntegerField()
	experience = models.IntegerField()

	def get_path(self, request):
		path = "http://" +  request.get_host() + "/detectives/" + str(self.id)
		return path
		
	def show_content(self, path, request):
		return { 
		'id': self.id,
		'name': self.name,
		'rate': self.rate,
		'experience': self.experience
		} 
		
	def __unicode__(self):
		return self.name

class Case(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=100)
	date = models.DateTimeField()
	clients = models.ManyToManyField(Client)
	suspects = models.ManyToManyField(Suspect)
	detective = models.ForeignKey(Detective)
	price = models.IntegerField()

	def get_path(self, request):
		path = "http://" +  request.get_host() + "/cases/" + str(self.id)
		return path

	def show_content(self, path, request):
	
		clients = []
		suspects = []
	
		for instance in self.clients.all():
			clients.append(instance.get_path(request))
			
		for instance in self.suspects.all():
			suspects.append(instance.get_path(request))
	
		return { 
		'id': self.id,
		'name': self.name,
		'date': self.date,
		'clients': clients,
		'suspects': suspects,
		'price': self.price
		} 
		
	def __unicode__(self):
		return self.name

