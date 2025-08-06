from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.


def sign_up(request):
    template_name = 'users/register.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, template_name, {'form': form})
    form = UserCreationForm()
    context = {'form': form}
    return render(request, template_name, context)


def sign_in(request):
    template_name = 'users/login.html'
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)

        form.add_error('password', 'Invalid username or password')
        return render(request, template_name, {'form': form})

    form = UserLoginForm()
    context = {'form': form}

    return render(request, template_name, context)


@require_POST
@login_required
def sign_out(request):
    logout(request)
    return redirect('home')




