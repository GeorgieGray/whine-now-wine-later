from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' }))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3' }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3' }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3' }))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm password"

    class Meta:
        model=User
        fields= ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3' }))