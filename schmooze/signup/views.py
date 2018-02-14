from django.shortcuts import render
from .models import Profile, Admin
from .forms import SignupForm, LoginForm, EmailForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth import models
# Create your views here.

def index(request):
	return render(request, 'index.html', context={})

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			p = Profile()
			user = form.save(commit = False)
			user.save()
			p.user = user
			p.username = form.cleaned_data.get('username')
			p.email = form.cleaned_data.get('email')
			p.package = form.cleaned_data.get('teams')
			p.save()
			return HttpResponseRedirect("/signup/")
		else:
			print(form.errors)
	else:
		form = SignupForm()

	return render(request, 'signup.html', context={'form' : form})

def login_view(request):
	form = LoginForm()

	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			adm = Admin.objects.all()
			a = list(adm)
			a = [str(x) for x in a]
			if username in a:
				login(request, user)
				return HttpResponseRedirect('/signup/email')
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/signup/profile')
	return render(request, 'login.html', {'form': form})

class ProfileDetailView(generic.DetailView):
	model = Profile
	# def get(self, request, *args, **kwargs):
	# 	user = Profile.objects.get(pk=self.kwargs['pk'])
	# 	context = {'profile' : profile}
	# 	return render(request, 'signup/profile.html', context)

def email(request):
	adm = Admin.objects.all()
	a = list(adm)
	a = [str(x) for x in a]
	if request.user.username in a: 
		if request.method == 'POST':
			form = EmailForm(request.POST)
			if form.is_valid():
				data = form.cleaned_data
				new_york_1 = [data["Giants"], data["Knicks"], data["Yankees"], data["Rangers"]]
				new_york_2 = [data["Jets"], data["Nets"], data["Mets"], data["Islanders"]]
				los_angeles = [data["Rams"], data["Chargers"], data["Lakers"], data["Clippers"], data["Dodgers"], data["Angels"], data["Kings"], data["Ducks"]]
				chicago = [data["Bears"], data["Bulls"], data["Cubs"], data["White_Sox"],  data["Blackhawks"]]
				wash = [data["Redskins"], data["Wizards"], data["Nationals"], data["Capitals"]]
				detroit = [data["Lions"], data["Pistons"], data["Tigers"], data["Red_Wings"]]

				print(new_york_1)
				print(new_york_2)
				print(los_angeles)
				print(chicago)
				print(wash)
				print(detroit)
		else:
			form = EmailForm()

		return render(request, 'signup/email.html', context={'form' : form})
	else:
		return HttpResponseRedirect("/signup/")
