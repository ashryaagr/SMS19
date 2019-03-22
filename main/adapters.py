from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter
from main.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
import json
import re


"""class SocialAccountAdapter(DefaultSocialAccountAdapter):


    def save_user(self, request, sociallogin, form=None):
        user = DefaultSocialAccountAdapter.save_user(
            self, request, sociallogin, form=form)
        if UserProfile.objects.filter(user=user).exists():
            pass
        else:
            new_user = UserProfile(user=user, name=user.get_full_name())
            new_user.save()
        return redirect('/')
"""        

        
class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):

        from allauth.account.utils import user_username, user_email, user_field

        data = form.cleaned_data
        name = data.get('name')
        email = data.get('email')
        username = data.get('username')
        user_email(user, email)
        user_username(user, username)
        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        user_field(user, 'name', name)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        
        return user
