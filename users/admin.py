from django.contrib import admin
from .models import Profile
# Here we are registaring the Profile model in the admin panel
admin.site.register(Profile)