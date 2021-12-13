from django.db import models
from hashlib import sha256
import base64

# Model odpowiedzialny za pojedyncze
# ogloszenie w aplikacji

class Pin(models.Model):

	# Pola z informacjami tekstowymi
	title = models.CharField(max_length = 100)
	email = models.CharField(max_length = 50)
	phone_number = models.CharField(max_length = 12, blank = True)
	facebook = models.CharField(max_length = 100, blank = True)
	address = models.CharField(max_length = 100, blank = True)
	description = models.CharField(max_length = 1000)
	
	# Haslo i obsluga hasla
	password = models.CharField(max_length = 50)

	def veryfiPassword(self, password_to_test):
		return self.password == password_to_test

	# Hashowanie i Odhashowywanie hasla
	def encodePassword(self):
		self.password = base64.b64encode(
			self.password.encode("ascii")
		).decode("ascii")
		
	def decodePassword(self):
		self.password = base64.b64decode(
			self.password.encode("ascii")
		).decode("ascii")
	
	# Pola wyboru i ich obsluga
	status_choices = [
		("A", "Aktualnie nie przyjmuję zleceń"),
		("B", "Gotowy do przyjęcia zleceń"),
	]
	status = models.CharField(
		max_length = 1,
		choices = status_choices,
		default = "B",
	)
	def getStatus(self):
		return dict(self.status_choices)[self.status]
	
	skills_choices = [
		("A", "Żółtodziób"),
		("B", "Niemiecki serwisant"),
		("C", "Polski serwisant"),
		("D", "Pro"),
		("E", "Leet"),
		("F", "Forest"),
	]
	skills = models.CharField(
		max_length = 1,
		choices = skills_choices,
		default = "A",
	)
	def getSkills(self):
		return dict(self.skills_choices)[self.skills]
	
	shipment_choices = [
		("A", "Nie"),
		("B", "Tak"),
	]
	shipment = models.CharField(
		max_length = 1,
		choices = shipment_choices,
		default = "B",
	)
	def getShipment(self):
		return dict(self.shipment_choices)[self.shipment]

	category_choices = [
		("A", "Naprawa komputerów / laptopów"),
		("B", "Naprawa sprzętu audio"),
		("C", "Naprawa smartfonów / tabletów"),
		("D", "Naprawa sprzętu retro"),
		("E", "Odnawianie sprawnego sprzętu retro"),
		("F", "Odnawianie sprawnego sprzętu"),
		("G", "Naprawa drobnej elektroniki"),
		("H", "Elektronik - wszystkonaprawiający"),
		("I", "Serwisant - wszstkonaprawiający"),
	]
	category = models.CharField(
		max_length = 1,
		choices = category_choices,
		default = "A",
	)
	def getCategory(self):
		return dict(self.category_choices)[self.category]
