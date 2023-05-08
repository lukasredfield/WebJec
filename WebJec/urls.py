"""WebJec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from WebJecApp import views
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="Home"),
    path('ministerios', views.ministerios, name="Ministerios"),
    path('mision', views.mision, name="Mision"),
    path('contacto', views.contacto, name="Contacto"),
    path('index', views.index, name="Index"),
    path('contact/', views.contact_view, name='contact_view'),
    path('mensaje/', views.mensaje, name='mensaje'),
]

