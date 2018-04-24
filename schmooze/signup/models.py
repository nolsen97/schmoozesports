from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	email = models.EmailField(null = True)
	package = models.CharField(null = True, max_length = 500)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.email

	def get_absolute_url(self):
		return reverse('profile', args=[str(self.id)])

class Admin(models.Model):
	username = models.CharField(max_length = 50, null=True)
	password = models.CharField(max_length = 255, null=True)
	
	def __str__(self):
		return self.username
