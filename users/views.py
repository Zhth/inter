from django.shortcuts import render

from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('webinter:index'))

def register(request):
    if request.method != 'POST':
        # Display blank registration form.   
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Log the user in, and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('webinter:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)