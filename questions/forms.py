""" from django import forms
from .models import User,Profile,Chapter


class authenticationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']


class qusetionForm(forms.ModelForm):
    class Meta:
        model=Chapter
        fields=('chapter',)
 """