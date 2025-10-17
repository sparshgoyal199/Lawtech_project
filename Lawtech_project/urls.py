"""
URL configuration for Lawtech_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from compoundInterest.views import *
from pythegoreanTriplet.views import *

urlpatterns = [
    path('calculate_interest_v1',calculate_interest_v1),
    path('calculate_interest_v2',calculate_interest_v2),
    path('calculate_pythegorean_template_v1',calculate_pythegorean_template_v1),
    path('calculate_pythegorean_template_v2',calculate_pythegorean_template_v2),
    path('admin/', admin.site.urls),
]
