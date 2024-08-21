from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from user.forms import LoginForm, RegisterForm


# python manage.py migrate

def login_page(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate( username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect('/user/')
    context['message error'] = 'Invalid username or password'
    context['form'] = LoginForm
    return render(request, 'login.html', context=context)


def logout_page(request):
    logout(request)
    return redirect('/login')

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data["username"],
                                            email=form.cleaned_data["email"],
                                            password=form.cleaned_data["password"],
                                            first_name=form.cleaned_data["first_name"],
                                            last_name=form.cleaned_data["last_name"],
                                            )
            user.save()
        return redirect('/login/')
    else:
        return render(request, 'register.html', context={'form': RegisterForm()})


@login_required
def user_page(request):

    return render(request, 'user_page.html', context={"username": request.user.username})
