from django.forms import ModelForm
from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
	c = (
		("Giants, Knicks, Yankees, Rangers", "The Classic New Yorker: Giants, Knicks, Yankees, Rangers"),
		("Jets, Nets, Mets, Islanders", "The I'm from Long Island, actually: Jets, Nets, Mets, Islanders"),
		("Rams, Chargers, Lakers, Clippers, Dodgers, Angels, Kings, Ducks", "The SoCal BroCal: Rams, Chargers, Lakers, Clippers, Dodgers, Angels, Kings, Ducks"),
		("Bears, Bulls, Cubs, White Sox, Blackhawks", "The Deep Dish: Bears, Bulls, Cubs, White Sox, Blackhawks"),
		("Redskins, Wizards, Nationals, Capitals", "The Washingtonian: Redskins, Wizards, Nationals, Capitals"),
		("Lions, Pistons, Tigers, Red Wings", "The Metro-Detroiter: Lions, Pistons, Tigers, Red Wings"),
	)

	teams = forms.ChoiceField(choices = c)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'teams']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)
