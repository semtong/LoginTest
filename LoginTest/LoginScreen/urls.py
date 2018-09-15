from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from LoginScreen.views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('main/', MainView.as_view(), name='main'),
    path('login/', include('django.contrib.auth.urls')),
    path('join/', TemplateView.as_view(template_name='join.html'), name='join'),
    path('sendToUserInfo/', Join.as_view()),
    path('main/detail/<int:post_id>', Detail.as_view(), name='detail'),
    path('main/detail/modify/<int:post_id>', Modify.as_view()),
    path('sendToUserModify/', SendModify.as_view(), name='board')
]