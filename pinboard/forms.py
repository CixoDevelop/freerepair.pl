from django import forms
from .models import Pin
from django.core import validators
from django.core.exceptions import ValidationError

# Formularz uzywany podczas walidacji
# wlasnosci ogloszenia przed usuneiciem
# lub modyfikacja
class PinboardLoginForm(forms.ModelForm):

	# tworzy formularz na podstawie modelu
	class Meta:
		model = Pin
		fields = (
			"email",
			"password",
		)
		labels = {
			"email": "Adres email z ogłoszenia",
			"password": "Hasło jakie ustawiłeś",
		}
		widgets = {
			"password": forms.TextInput(attrs = {"type": "password"}),
		}
	
	def clean_email(self):
		# Funkcja sprawdza czy email jest
		# w bazie danych, jezeli jest
		# to zwraca konczy poprawnie,
		# inaczej wywoluje blad
		
		try:
			self.pin = Pin.objects.get(email = self.cleaned_data["email"])
		except:
			raise ValidationError("Takiego email-a nie ma!")
		
		return self.cleaned_data["email"]	
		
	def clean_password(self):
		# Sprawdzay czy wczytane ogloszenie jest
		# zabezpieczone tym samym haslem, jakie
		# podal uzytkownik i jezeli tak
		# idzie dalej, w przeciwnym wypadku zwraca blad

		try:
			self.pin.decodePassword()
			
			if self.pin.veryfiPassword(self.getPassword()):
				return self.cleaned_data["password"]
				
			raise ValueError
		except:
			raise ValidationError("Hasło jest błędne!")
	
	def getPassword(self):
		return self.cleaned_data["password"]

# Formularz odpowiedzialny za edycje oraz
# dodawanie ogloszen
class PinboardAddEditForm(forms.ModelForm):
	
	# Tworzenie pol formularza z modelu
	class Meta:
		model = Pin
		fields = (
			'title',
			'email',
			'description',
			'phone_number',
			'facebook',
			'address',
			'status',
			'skills',
			'shipment',
			'password',
			'category',
		)
		labels = {
			"title": "Tytuł",
			"email": "Adres email",
			"phone_number": "Numer telefonu (opcjonalne)",
			"facebook": "Konto facebook (opcjonalne)",
			"address": "Adres zamieszkania (opcjonalne)",
			"status": "Jestem gotowy na przyjmowanie zleceń",
			"skills": "Poziom moich umiejętności",
			"shipment": "Czy przyjmuję zlecenia za pośrednictwem poczty/kuriera",
			"password": "Hasło (wymagane przy późniejszej edycji, 8-30 znaków)",
			"description": "Opisz swoją działalność (40-1000 znaków)",
			"category": "Wybierz kategorie która najlepej pasuj do Twojej działalności",
			
		}
		widgets = {
			"password": forms.TextInput(attrs = {"type": "password"}),
		}

	# to pole pozwala sprawdzic czy uzytkownik
	# nie zrobil literowki wprowadzajac haslo	
	password_repeat = forms.CharField(
		max_length = 50, 
		widget = forms.TextInput(attrs = {"type": "password"}), 
		label = "Powtórz hasło",
	)
	
	# Funkcje weryfikujace czy podane dane sa prawidlowe
	def clean_title(self):
		if(
			len(self.cleaned_data["title"]) < 4 or 
			len(self.cleaned_data["title"]) > 100
		  ):
				
			raise ValidationError("Prawidłowa dłogość tytułu to 4-100 znaków!")
			
		return self.cleaned_data["title"]

	def clean_description(self):
		if(
			len(self.cleaned_data["description"]) < 40 or
			len(self.cleaned_data["description"]) > 1000
		):
			raise ValidationError("Prawidłowej długości opis to 40-1000 znaków!")

		return self.cleaned_data["description"]
		
	def clean_email(self):
		validators.EmailValidator(
			message = "Adres E-Mail nie jest prawidłowy!",
		)(self.cleaned_data["email"])
		
		return self.cleaned_data["email"]	
		
	def clean_phone_number(self):
		if len(self.cleaned_data['phone_number']) != 0:
			validators.RegexValidator(
				regex = "[0-9]{3}-[0-9]{3}-[0-9]{3}",
				message = "Podano błędny numer telefonu. Poprawny jest format 123-456-789!",
			)(self.cleaned_data['phone_number'])
		
		return self.cleaned_data['phone_number']
	
	# Funkcje sprawdzajace czy haslo spelnia wymagania
	# co do dlugosci oraz czy oba hasla sa identyczne	
	def clean_password(self):
		if(
			len(self.cleaned_data["password"]) < 8 or
			len(self.cleaned_data["password"]) > 30
		  ):
			
			raise ValidationError("Hasło musi mieć nie mniej niż 8 i nie więcej niż 30 znaków!")
		
		return self.cleaned_data["password"]
		
	def clean_password_repeat(self):
		if "password" not in self.cleaned_data:
			raise ValidationError("")
			
		if(
			self.cleaned_data["password"] != 
			self.cleaned_data["password_repeat"]
		  ):
				
			raise ValidationError("Hasła nie zgadzają się!")
			
		return self.cleaned_data["password_repeat"]
				
	# Funckja zwracajaca haslo do wstawienia do bazy danych		
	def getPassword(self):
		return self.cleaned_data["password"]	
