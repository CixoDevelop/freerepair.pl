from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import forms
from .models import Pin


def show_pins(request):
	# Widok glowny, pokazuje wszyskie ogloszenia
	# ewentualnie przeszkuje ogloszenia na podstawie
	# danych z GET
	
	pins = Pin.objects.all()
	hello = True
	
	if request.method == "GET":		
		if(
			"category" in request.GET and
			request.GET.get("category") != ""
		  ):
			hello = False
			pins = pins.filter(category = request.GET.get("category"))
			
		if(
			"search" in request.GET and
			request.GET.get("search") != ""
		  ):
			hello = False
			pins = pins.filter(title__contains = request.GET.get("search"))
			
	return render(
		request,
		"pins/pin.html",
		{
			"pins": pins,
			"categories": Pin.category_choices,
			"hello": hello,
		},
	)

def remove_pin(request):
	# Widok pozwala usunac pin, jezeli pin juz
	# nie istnieje ewentualnie uzytkownik nie
	# potwierdzil iz to on wystawil ogloszenie
	# to przekieruje do odpowiedniej strony
	
	try:
		# jezeli uda sie wyciagnac ogloszenie
		# z bazy danych
		pin = Pin.objects.get(email = request.session["actual_pin"])

		# to je usuwa
		pin.delete()

		# a potem usuwa walidacje i przekierowuje
		del request.session["actual_pin"]
		return HttpResponseRedirect("/")

	except:
		return HttpResponseRedirect("/zaloguj")

def add_pin(request):
	# Widok pozawalajacy dodac wlasne ogloszenie
	# po dodaniu uzytkownik zostanie przekierowany
	# na powrot do strony glownej

	# tworzy szablon 
	form = forms.PinboardAddEditForm()

	# jezli jakis szablon jest przeslany
	if request.method == "POST":
		form = forms.PinboardAddEditForm(request.POST)

		# to nastepuje walidacja
		if form.is_valid():

			# sprawdza czy email-a nie ma w bazie danych
			try:
				Pin.objects.get(email = form.cleaned_data["email"])
				form.add_error("email", "Niestety, ale taki email ma już przypisane ogłoszenie!")
			
			except:
				pin = form.save(commit = False)
				pin.encodePassword()
				pin.save()
				return HttpResponseRedirect("/")
			
	return render(
		request,
		"pins/form.html",
		{
			"add": True,
			"form": form,
		},
	)

def login_pin(request):
	# Widok strony pozwalajacy na walidacje
	# tego iz ogloszenie nalezy do uzytkownika
	# ktury chce je zmodyfikowac lub usunac

	# tworzy pusty szablon		
	form = forms.PinboardLoginForm()

	# natomiast jezeli jest juz cos przeslane
	if request.method == "POST":
		form = forms.PinboardLoginForm(request.POST)

		# to proboje to zwalidowac
		if form.is_valid():
			request.session["actual_pin"] = form.cleaned_data["email"]
			return HttpResponseRedirect("/edytuj")

	return render(
		request,
		"pins/form.html",
		{
			"login": True,
			"form": form,
		},
	)
	

def edit_pin(request):
	# Widok pozwala na edycje ogloszenia
	# jezeli uzytkownik nie jest zwalidowany
	# to zostanei na ta podstrone oddelegowany

	# proboje czy uzytkownik jest zwalidowany
	# a ogloszenie istnieje, jezeli nie to odsyla
	try:
		pin = Pin.objects.get(email = request.session["actual_pin"])
	except:
		return HttpResponseRedirect("/zaloguj")

	# ogloszenie jest zaladowane,
	# wiec nalezy odhashowac haslo
	pin.decodePassword()

	# formularz, przy czym powtorzenie hasla
	# rowniez jest ustawione, aby uzytkownik
	# nie musial przepisywac 
	form = forms.PinboardAddEditForm(
		instance = pin,
		initial = {"password_repeat": pin.password},
	)

	# jezeli formularz zostal przeslany
	# to zweryfikoj go
	if request.method == "POST":
		form = forms.PinboardAddEditForm(
			request.POST,
			instance = pin,
		)
		
		# a jezeli jest poprawny, to zapisz
		if form.is_valid():
			pin_to_save = form.save(commit = False)
			pin_to_save.encodePassword()
			pin_to_save.save()

			# usun walidacje oraz prekieroj na glowna
			del request.session["actual_pin"]
			return HttpResponseRedirect("/")

	return render(
		request,
		"pins/form.html",
		{
			"edit": True,
			"form": form,
		},
	)

# Strona statyczna z regulaminem, ktora
# posiada funkcje poniewaz jest renderowana

def regulamin(request):
	return render(
		request,
		"pins/regulamin.html",
		{},
	)
