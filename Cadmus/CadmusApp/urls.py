from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path('', form_continent, name="Cadmus Menu"),
    path('<int:id>', form_continent, name="continent_update"),
    path('delete/<int:id>/', delete_continent, name="continent_delete"),
    path('table/', view_continent, name="Tabelas"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('base_generic/', base),
]

