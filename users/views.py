from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import UserForm

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

