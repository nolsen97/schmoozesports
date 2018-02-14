from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	username = models.CharField(null = True, max_length = 300)
	email = models.EmailField(null = True)
	package = models.CharField(null = True, max_length = 500)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return reverse('profile', args=[str(self.id)])

class Admin(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.user.username
