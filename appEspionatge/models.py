from django.db import models

class Client(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=100)
	hide_id = models.BooleanField(default=False)

	def get_path(self, request):
		path = "http://" +  request.get_host() + "/clients/" + str(self.id)
		return path

	def __unicode__(self):
		return self.name		
	
class Suspect(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=100)
	history = models.TextField(max_length=200)

	def get_path(self, request):
		path = "http://" +  request.get_host() + "/suspects/" + str(self.id)
		return path		
	
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

	def __unicode__(self):
		return self.name

