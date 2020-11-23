from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile

User = get_user_model()

# A signal is a way to link multiple elements of the website that are affected by the same event
# In this example we want to create a new profile for each new user.
# Inside the forms.py file we declaired in the Meta class that we are creating a User instance when we complete the form
# And in the views.py file we are saving the User when there is a post request (clicking the button) 
# Here we are connecting the 2, the create profile will receive (because of the decorator) the User that was sent from the form
# and only when there is a save function called (like in the register) (thats why there is a post_save)
# If there is a new profile, update the data base with the Profile table

@receiver(post_save, sender=User)
 #pylint: disable=unused-argument
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# And here we are doing the same but we don't need to check if the profile exist because we need to update it
@receiver(post_save, sender=User)
#pylint: disable=unused-argument
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    