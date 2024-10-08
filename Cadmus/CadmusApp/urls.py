from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

app_name = 'CadmusApp'

urlpatterns = [
    path('', home, name="Cadmus Menu"),

    # Paths research
    path('research/', view_research, name="ResearchTable"),
    path('research/create/', form_research, name="ResearchCreate"),
    path('research/update/<int:id>', form_research, name="ResearchUpdate"),
    path('research/delete/<int:id>/', delete_research, name="ResearchDelete"),

    # Paths research_group
    path('researchGroup/', view_researchGroup, name="ResearchGroupTable"),
    path('researchGroup/create/', form_researchGroup, name="ResearchGroupCreate"),
    path('researchGroup/update/<int:id>', form_researchGroup, name="ResearchGroupUpdate"),
    path('researchGroup/delete/<int:id>/', delete_researchGroup, name="ResearchGroupDelete"),

    # Paths
    path('<int:id>', form_research, name="research_update"),
    path('delete/<int:id>/', delete_research, name="research_delete"),
    path('table/', view_research, name="Tabelas"),

    # Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('base_generic/', base),
]
