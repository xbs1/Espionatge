from django.db import models

class Client(models.Model):
	name = models.TextField(max_length=100)
	#case = models.ForeignKey(Case)
	
class Suspect(models.Model):
	name = models.TextField(max_length=100)
	#case = models.ForeignKey(Case)

class Detective(models.Model):
	name = models.TextField(max_length=100)
	#case = models.ForeignKey(Case)

class Case(models.Model):
	name = models.TextField(max_length=100)
	date = models.DateTimeField()
	client = models.ForeignKey(Client)
	suspect = models.ForeignKey(Suspect)
	detective = models.ForeignKey(Detective)
	price = models.IntegerField()

