from django.shortcuts import render
from .models import Profile
from .forms import SignupForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from django.views import generic
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
			return HttpResponseRedirect("/signup")
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

			if user is not None:
				login(request, user)
				return HttpResponseRedirect('profile.html')
	return render(request, 'login.html', {'form': form})

class ProfileDetailView(generic.DetailView):
	model = Profile
	def get(self, request, *args, **kwargs):
		context = {'profile' : profile}
		return render(request, 'profile.html', context)