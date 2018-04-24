from django.shortcuts import render
from .models import Profile, Admin
from .forms import SignupForm, LoginForm, EmailForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# from django.template import sampleemail
# Create your views here.

def index(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			p = Profile()
			p.email = form.cleaned_data.get('email')
			p.package = form.cleaned_data.get('teams')
			p.save()
			request.session['email'] = p.email
			return HttpResponseRedirect("/signup/success/")
		else:
			print(form.errors)
	else:
		form = SignupForm()

	return render(request, 'index.html', context={'form':form})

def success(request):
	# send_mail(
 #    'Thank you for signing up!',
 #    'We have recieved your email and sport preferences. You should start recieving emails shortly.',
 #    request.session['email'],
 #    ['nso4wg@virginia.edu'],
 #    fail_silently=False,
	# )
	return render(request, 'success.html', context={})

# def signup(request):
# 	if request.method == 'POST':
# 		form = SignupForm(request.POST)
# 		if form.is_valid():
# 			p = Profile()
# 			user = form.save(commit = False)
# 			user.save()
# 			p.user = user
# 			p.username = form.cleaned_data.get('username')
# 			p.email = form.cleaned_data.get('email')
# 			p.package = form.cleaned_data.get('teams')
# 			p.save()
# 			return HttpResponseRedirect("/signup/")
# 		else:
# 			print(form.errors)
# 	else:
# 		form = SignupForm()

# 	return render(request, 'signup.html', context={'form' : form})

def login_view(request):
	form = LoginForm()

	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			try:
				a = Admin.objects.all().get(username=username)
				if (a.password == password):
					request.session['username'] = a.username
					return HttpResponseRedirect('/signup/email/')
			except:
				pass
	else:
		form = LoginForm()

	return render(request, 'login.html', {'form': form})

# class ProfileDetailView(generic.DetailView):
# 	model = Profile
# 	def get(self, request, *args, **kwargs):
# 		user = Profile.objects.get(pk=self.kwargs['pk'])
# 		context = {'profile' : profile}
# 		return render(request, 'signup/profile.html', context)

def email(request):
	try:
	 	Admin.objects.all().get(username=request.session['username'])
		if request.method == 'POST':
			form = EmailForm(request.POST)
			if form.is_valid():
				data = form.cleaned_data
				new_york_1 = [str(data["Giants"]), str(data["Knicks"]), str(data["Yankees"]), str(data["Rangers"])]
				new_york_2 = [str(data["Jets"]), str(data["Nets"]), str(data["Mets"]), str(data["Islanders"])]
				los_angeles = [str(data["Rams"]), str(data["Chargers"]), str(data["Lakers"]), str(data["Clippers"]), str(data["Dodgers"]), str(data["Angels"]), str(data["Kings"]), str(data["Ducks"])]
				chicago = [str(data["Bears"]), str(data["Bulls"]), str(data["Cubs"]), str(data["White_Sox"]),  str(data["Blackhawks"])]
				wash = [str(data["Redskins"]), str(data["Wizards"]), str(data["Nationals"]), str(data["Capitals"])]
				detroit = [str(data["Lions"]), str(data["Pistons"]), str(data["Tigers"]), str(data["Red_Wings"])]

				# print(new_york_1[1])
				# print(new_york_2)
				# print(los_angeles)
				# print(chicago)
				# print(wash)
				# print(detroit)

				new_york_1_subs = Profile.objects.filter(package="Giants, Knicks, Yankees, Rangers").values('email')
				new_york_1_subs = list(new_york_1_subs)
				to = []
				for e in range(len(new_york_1_subs)):
					to.append(str(new_york_1_subs[e].get('email')))

				print(to)
				subject = 'test'
				from_email = 'nate.olsen97@gmail.com'
				
				
				html_content = render_to_string('sampleemail.html', {"data": new_york_1})
				msg = EmailMultiAlternatives(subject, '', from_email, to)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
		else:
			form = EmailForm()

		return render(request, 'signup/email.html', context={'form' : form})
	except:
		return HttpResponseRedirect('/signup/')