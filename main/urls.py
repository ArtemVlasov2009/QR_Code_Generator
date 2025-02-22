"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_home, name='home'),
    path('registration/', render_registration, name='registration'),
    path('authorization/', render_authorization, name='authorization'),
    path('logout/', logout_user, name = "logout"),
    path('contacts/', render_contacts, name='contacts'),
    path('generator/', render_generator, name='generator'),
    path('history_gen/', render_history_gen, name='history_generations'),
]
