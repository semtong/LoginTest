from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from LoginScreen.views import *

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', include('django.contrib.auth.urls')),
    path('join/', TemplateView.as_view(template_name='join.html'), name='join'),
    path('sendToUserInfo/', Join.as_view())
]