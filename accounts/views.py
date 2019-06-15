from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, CaseInsensitiveUserCreationForm


from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('aarya')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def newsignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('aarya')
    else:
        form = SignUpForm()
    return render(request, 'newsignup.html', {'form': form})


#User creation form with case insensitive user names
def newsafesignup(request):
    if request.method == 'POST':
        form = CaseInsensitiveUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('aarya')
    else:
        form = CaseInsensitiveUserCreationForm()
    return render(request, 'newsafesignup.html', {'form': form})

