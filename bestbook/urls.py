"""
URL configuration for bestbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('register/', views.register, name="registration"),
    path('login/', views.log_in, name="loging_in"),
    path('logout/', views.log_out, name="loging_out"),
    path('login_fail/', views.login_fail, name="loging_fail"),
    path('', include('polls.urls')),
    # path('search_results/', views.search_results, name="results")

]
