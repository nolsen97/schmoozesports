from django.contrib import admin

# Register your models here.
from .models import Profile, Admin
admin.site.register(Profile)
admin.site.register(Admin)