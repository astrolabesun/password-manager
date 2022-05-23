from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def login_view(request):
    # if POST for login, authenticate
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username, password)
        if user != None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid credentials!')
    # otherwise, if user already logged in, just render their profile
    # if not logged in, just keep displaying the login form
    return render(request, 'index.html')


def registration_view(request):
    # if POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # upon registration, take user to their profile page
            return redirect('profile')
        else:
            messages.error(request, 'Please give valid info to the form')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home_login')


@login_required(login_url='home_login')
def profile(request, pk):
    # grab all the credentials the user stored in the manager, if any
    user = User.objects.get(id=pk)
    return render(request, 'profile.html')