from django.urls import path
from . import views

urlpatterns = [
	path("", views.show_pins, name = "show_pins"),
	path("dodaj", views.add_pin, name = "add_pin"),
	path("edytuj", views.edit_pin, name = "edit_pin"),
	path("usun", views.remove_pin, name = "remove_pin"),
	path("zaloguj", views.login_pin, name="login_pin"),
	path("regulamin", views.regulamin, name="regulamin"),
]
