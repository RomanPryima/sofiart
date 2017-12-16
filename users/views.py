from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import Http404


def signup(request):
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

