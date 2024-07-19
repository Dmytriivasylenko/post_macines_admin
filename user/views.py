from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

#def login(request)
def user_page(request):
    return HttpResponse(" Hello world, You're at the- user_page")

def login_page(request):
    return HttpResponse(" Hello world, You're at the- login_page")


def register_page(request):
    return HttpResponse(" Hello world, You're at the- register_page")