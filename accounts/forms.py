from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser

from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CaseInsensitiveUserCreationForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(CaseInsensitiveUserCreationForm, self).clean()
        username = cleaned_data.get('username')
        if username and User.objects.filter(username__iexact=username).exists():
            self.add_error('username', 'A user with that username already exists.')
        return cleaned_data

class UpdateProfileForm(forms.ModelForm):
    display_name = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('display_name', 'first_name', 'last_name')

    def clean_displayname(self):
        display_name = self.cleaned_data.get(display_name)

        if display_name and User.objects.filter(display_name=display_name).exclude(username=username).count:
            raise forms.ValidationError('This Display Name is already in use. Please provide a different Display Name.')
        return display_name

