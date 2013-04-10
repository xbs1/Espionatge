from django.db import models

class Client(models.Model):
	name = models.TextField(max_length=100)

	def __unicode__(self):
		return self.name
	
class Suspect(models.Model):
	name = models.TextField(max_length=100)

	def __unicode__(self):
		return self.name

class Detective(models.Model):
	name = models.TextField(max_length=100)

	def __unicode__(self):
		return self.name

class Case(models.Model):
	name = models.TextField(max_length=100)
	date = models.DateTimeField()
	client = models.ForeignKey(Client)
	suspect = models.ForeignKey(Suspect)
	detective = models.ForeignKey(Detective)
	price = models.IntegerField()

	def __unicode__(self):
		return self.name

