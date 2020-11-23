from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

User = get_user_model()

# Here we are creating a new regestration form by inhereting from the UserCreationForm and adding an email to it
# And in the Meta class we are defining that we want to pass a User instance from the form (the model variable)
# and in the fields we want to show in the form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Here we are creating a new form that will be showed on the profile for the user to update his info
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']