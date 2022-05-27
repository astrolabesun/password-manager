from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Credentials
from .forms import CredentialsForm

# Create your views here.

def login_view(request):
    # if user already authenticated, take them to their profile
    if request.user.is_authenticated:
        return redirect('profile', request.user.pk)

    # if POST for login, authenticate
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('profile', user.pk)
        else:
            messages.error(request, 'Invalid credentials!')
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
            return redirect('profile', user.pk)
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
def profile_view(request, pk):
    # grab all the credentials the user stored in the manager, if any
    user = User.objects.get(id=pk)
    # load user info if the user's stuff belongs to them
    # and prevent an authenticated user from accessing other users' profiles
    if request.user == user:
        creds = Credentials.objects.filter(user_id=pk)
        context = {'user':user, 'creds':creds}
        return render(request, 'profile.html', context)
    else:
        return HttpResponseForbidden('Stay in your profile!')


@login_required(login_url='home_login')
def add_creds_view(request, pk):
    # if POST, grab the creds the user wants to
    if request.method == "POST":
        # need to make a credentials fill out form
        creds_form = CredentialsForm(request.POST)
        # save the data to the db, if valid
        if creds_form.is_valid():
            user = User.objects.get(id=pk)
            if user is not None:
                # user_id is a required field, so before committing, set it to the current user
                creds = creds_form.save(commit=False)
                creds.user_id = user
                creds.save()
                return redirect('profile', user.pk)
            else:
                messages.error(request, 'Credentials storing failed. User not found')
    else:
        creds_form = CredentialsForm()
    context = {'form':creds_form}
    return render(request, 'add_creds.html', context)


@login_required(login_url='home_login')
def update_creds_view(request, pk):
    # make sure the creds belong to the user before updating
    # grab the credentials in question by its id
    creds = Credentials.objects.get(pk=pk)
    if request.method == "POST":
        if request.user == creds.user_id:
            # save the changes, take user back to profile
            form = CredentialsForm(request.POST, instance=creds)
            if form.is_valid():
                form.save()
            return redirect('profile', request.user.pk)
        else:
            messages.error(request, 'These are not your credentials!!')
    else:
        form = CredentialsForm(instance=creds)
    context = {'creds':creds, 'form':form}
    return render(request, 'update_creds.html', context)


@login_required(login_url='home_login')
def delete_creds_view(request, pk):
    # make sure the creds belong to the user before deleting
    creds = Credentials.objects.get(pk=pk)
    if request.user == creds.user_id:
        creds.delete()
    else:
        messages.error(request, 'These are not your credentials!!')
    return redirect('profile', request.user.pk)
