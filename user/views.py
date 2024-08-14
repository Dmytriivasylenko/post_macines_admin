from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# python manage.py migrate

def login_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/user/')
        else:
            context['message error'] = 'Invalid username or password'

    return render(request, 'login.html', context=context)


def logout_page(request):
    logout(request)
    return redirect('/login')

def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name,)
        user.save()
        return redirect('/login/')
    else:
        return render(request, 'register.html')


@login_required
def user_page(request):

    return render(request, 'user_page.html', context={"username": request.user.username})
