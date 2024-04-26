"""
URL configuration for traffictracker_dj project.

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
from django.urls import path
from django.conf.urls import include
from static_pages.views import index, about, contact, success, welcome, flan_recipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("success/", success, name="success"),
    path("welcome/", welcome, name="welcome"),
    path("recipe/<slug:slug>/", flan_recipe, name="flan_recipe"),
    path("accounts/", include('django.contrib.auth.urls')),
]
# path('getting-started/<slug:prglangcat_slug>/<slug:prg_slug>', views.programmingLanguageTutorial, name="tutorial-page"),
