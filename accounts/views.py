from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            authenticate(username=user.username, password=user.password)

            if user is not None:
                login(request, user)

                return redirect ('/dashboard/')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})





