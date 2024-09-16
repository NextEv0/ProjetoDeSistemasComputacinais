from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('tables/', crud),
]

