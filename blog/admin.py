from django.contrib import admin
from .models import Post
# Here we are registering the Post model that we created in the admin panel, we need to do this for every new model that we want to see there 
admin.site.register(Post)