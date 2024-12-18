"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
    path('', include('your_app.urls')),  # Include URLs from your custom app
    path('', views.home, name='home'),                  # Home page URL
    path('login/', views.login_view, name='login'),     # Login page URL
    path('register/', views.register_view,
         name='register'),  # Registration page UR
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    # Ensure you have a 'home' view if you redirect there
    path('home/', views.home, name='home'),
]
