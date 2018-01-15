from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField


class UserForm(UserCreationForm):
    username = forms.CharField(label='Псевдо')
    first_name = forms.CharField(label="Ім'я", required=False)
    last_name = forms.CharField(label="Прізвище", required=False)
    email = forms.EmailField(label='Електронна поштова скринька')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        try:
            user.first_name = self.cleaned_data['first_name']
        except:
            pass
        try:
            user.last_name = self.cleaned_data['last_name']
        except:
            pass
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class LoginForm(AuthenticationForm):

    username = UsernameField(
        label='Псевдо',
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput,
    )

    error_messages = {
        'invalid_login': (
            "Будь ласка, введіть корректне ім'я і пароль. Зауважте, що обидва "
            "поля чутливі до регістру."
        ),
        'inactive': "Цей користувач - неактивний.",
    }

    class Meta:
        model = User
        fields = ['username']
