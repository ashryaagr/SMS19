"""SMS19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from main import views
from django.conf.urls import url


urlpatterns = [

    path('accounts/logout/', views.user_logout, name='user_logout'),
    path('accounts/forgot_password/', views.user_forgot_password,
         name='user_forgot_password'),
    path('accounts/activate/<slug:uidb64>/<slug:token>', views.activate, name='activate'),
    path('admin/', admin.site.urls),
    path('', views.game, name='game'),    

    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.user_login, name='user_login'),
    path('accounts/', include('allauth.urls')),
    ]
