from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfoModel


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        # Tienen que ser en inglés al estar utilizando el registro por defecto de django. Aquí tuve el fallo gordo
        fields = ('username', 'email', 'password')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfoModel
        fields = ('portfolio_site', 'profile_pic')