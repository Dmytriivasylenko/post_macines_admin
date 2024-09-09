"""
URL configuration for post_macines_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views import View
import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parcel/', include('parcel.urls')),
    path('post_machine/', include('post_machine.urls')),
    #path('login/', user.views.login_page),
    #path('logout/', user.views.logout_page),
    #path('register/', user.views.register_page),
    #path('user/', include('user.urls')),
    path('login/', user.LoginView.as_view(), name='login'),
    path('register/', user.RegisterView.as_view(), name='register'),
]
