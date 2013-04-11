from django.db import models

class Client(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=100)
	hide_id = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name		
	
class Suspect(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=100)
	history = models.TextField(max_length=200)

	def __unicode__(self):
		return self.name

class Detective(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=100)
	rate = models.IntegerField()
	experience = models.IntegerField()

	def __unicode__(self):
		return self.name

class Case(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=100)
	date = models.DateTimeField()
	client = models.ForeignKey(Client)
	#clients = models.ManyToManyField(Client)
	suspect = models.ForeignKey(Suspect)
	#suspects = models.ManyToManyField(Suspect)
	detective = models.ForeignKey(Detective)
	#detectives = models.ManyToManyField(Detective)
	price = models.IntegerField()

	def __unicode__(self):
		return self.name

