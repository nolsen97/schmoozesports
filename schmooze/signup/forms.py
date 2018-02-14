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

class EmailForm(forms.Form):
	Giants = forms.CharField(max_length=500)
	Knicks = forms.CharField(max_length=500)
	Yankees = forms.CharField(max_length=500)
	Rangers = forms.CharField(max_length=500)
	Jets = forms.CharField(max_length=500)
	Nets = forms.CharField(max_length=500)
	Mets = forms.CharField(max_length=500)
	Islanders = forms.CharField(max_length=500)
	Rams = forms.CharField(max_length=500)
	Chargers = forms.CharField(max_length=500)
	Lakers = forms.CharField(max_length=500)
	Clippers = forms.CharField(max_length=500)
	Dodgers = forms.CharField(max_length=500)
	Angels = forms.CharField(max_length=500)
	Kings = forms.CharField(max_length=500)
	Ducks = forms.CharField(max_length=500)
	Bears = forms.CharField(max_length=500)
	Bulls = forms.CharField(max_length=500)
	Cubs = forms.CharField(max_length=500)
	White_Sox = forms.CharField(max_length=500)
	Blackhawks = forms.CharField(max_length=500)
	Redskins = forms.CharField(max_length=500)
	Wizards = forms.CharField(max_length=500)
	Nationals = forms.CharField(max_length=500)
	Capitals = forms.CharField(max_length=500)
	Lions = forms.CharField(max_length=500)
	Pistons = forms.CharField(max_length=500)
	Tigers = forms.CharField(max_length=500)
	Red_Wings = forms.CharField(max_length=500)