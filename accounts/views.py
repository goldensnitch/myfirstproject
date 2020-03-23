from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login
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



def blogregistration(request):
    if request.method == 'POST':
        form = CaseInsensitiveUserCreationForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password1'] != form.cleaned_data['password2']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password1']
                )
                user.save()

                newuser = authenticate(username=request.POST['username'], password=request.POST['password1'])

                if newuser is not None:
                    login(request,newuser)
                    return redirect('aarya')
    else:
        form = CaseInsensitiveUserCreationForm()

    return render(request, 'blog-registration.html', {'form': form})

