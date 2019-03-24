from allauth.account.forms import SignupForm
from django import forms
from .validators import SpecialCharacterValidator
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile

class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Username', validators=[SpecialCharacterValidator])
    name = forms.CharField(max_length=30, label='Name', validators=[SpecialCharacterValidator])

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.save()
        return user


class UserProfileCreationForm(UserCreationForm):
    name = forms.CharField(max_length=30, label='Name',
                     validators=[SpecialCharacterValidator])
    class Meta(UserCreationForm):
        model = UserProfile
        fields = ('username', 'email', 'name', 'password')


class UserProfileChangeForm(UserChangeForm):
    name = forms.CharField(max_length=30, label='Name',
                     validators=[SpecialCharacterValidator])
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'name', 'password')
