from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


# Here we are creating the views that we set in the project urls.py file
# in the register view we need to load the page twice, once when we get inside and the second time after we press the sign in button
# After we are pressing the button the http request is changed from GET to POST, 
# and then we know if we need to save the data and redirect with a message
# Or to show the form again to the user
# In the end we will always render the page with the request itself, the html file that we want to load, 
# and the data we want to pass to the html (in this case the form)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

# Here we are using login required decorator to prohibit the access to the profile view unless there is a user logged in
# Also, we added the forms from the forms.py file and passed them to the profile.html file
# Here we also made sure to validate the forms after the update button was clicked and save them in the database
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form= ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.profile)
    contex = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context=contex)

