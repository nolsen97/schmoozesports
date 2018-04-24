from django.forms import ModelForm
from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(forms.Form):
	c = (
		("Giants, Knicks, Yankees, Rangers", "The Classic New Yorker: Giants, Knicks, Yankees, Rangers"),
		("Jets, Nets, Mets, Islanders", "The I'm from Long Island, actually: Jets, Nets, Mets, Islanders"),
		("Rams, Chargers, Lakers, Clippers, Dodgers, Angels, Kings, Ducks", "The SoCal BroCal: Rams, Chargers, Lakers, Clippers, Dodgers, Angels, Kings, Ducks"),
		("Bears, Bulls, Cubs, White Sox, Blackhawks", "The Deep Dish: Bears, Bulls, Cubs, White Sox, Blackhawks"),
		("Redskins, Wizards, Nationals, Capitals", "The Washingtonian: Redskins, Wizards, Nationals, Capitals"),
		("Lions, Pistons, Tigers, Red Wings", "The Metro-Detroiter: Lions, Pistons, Tigers, Red Wings"),
	)
	email = forms.EmailField(max_length=30)
	teams = forms.ChoiceField(choices = c)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)

class EmailForm(forms.Form):
	Giants = forms.CharField(max_length=500, required=False)
	Knicks = forms.CharField(max_length=500, required=False)
	Yankees = forms.CharField(max_length=500, required=False)
	Rangers = forms.CharField(max_length=500, required=False)
	Jets = forms.CharField(max_length=500, required=False)
	Nets = forms.CharField(max_length=500, required=False)
	Mets = forms.CharField(max_length=500, required=False)
	Islanders = forms.CharField(max_length=500, required=False)
	Rams = forms.CharField(max_length=500, required=False)
	Chargers = forms.CharField(max_length=500, required=False)
	Lakers = forms.CharField(max_length=500, required=False)
	Clippers = forms.CharField(max_length=500, required=False)
	Dodgers = forms.CharField(max_length=500, required=False)
	Angels = forms.CharField(max_length=500, required=False)
	Kings = forms.CharField(max_length=500, required=False)
	Ducks = forms.CharField(max_length=500, required=False)
	Bears = forms.CharField(max_length=500, required=False) 
	Bulls = forms.CharField(max_length=500, required=False)
	Cubs = forms.CharField(max_length=500, required=False)
	White_Sox = forms.CharField(max_length=500, required=False)
	Blackhawks = forms.CharField(max_length=500, required=False)
	Redskins = forms.CharField(max_length=500, required=False)
	Wizards = forms.CharField(max_length=500, required=False)
	Nationals = forms.CharField(max_length=500, required=False)
	Capitals = forms.CharField(max_length=500, required=False)
	Lions = forms.CharField(max_length=500, required=False)
	Pistons = forms.CharField(max_length=500, required=False)
	Tigers = forms.CharField(max_length=500, required=False)
	Red_Wings = forms.CharField(max_length=500, required=False)