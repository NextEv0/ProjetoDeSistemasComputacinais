from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
import pandas as pd
from .models import *
from .forms import *
from django.db import connection

# Página inicial (somente acessível após login)
@login_required
def home(request):
    return render(request, "index.html")

# TABELA CONTINENTE
def view_continent(request):
    context = {'view_continent': Continent.objects.all()}
    return render(request, "tables_copy.html", context)

def form_continent(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ContinentForm()
        else:
            continent = Continent.objects.get(pk=id)
            form = ContinentForm(instance=continent)
        return render(request, "tables_form.html", {'continent_form': form})
    else:
        if id == 0:
            form = ContinentForm(request.POST)
        else:
            continent = Continent.objects.get(pk=id)
            form = ContinentForm(request.POST, instance=continent)
        if form.is_valid():
            form.save()
        return redirect('table/')

def delete_continent(request, id):
    continent = Continent.objects.get(pk=id)
    continent.delete()
    return redirect('/table/')

# Registro de novos usuários
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Faz login automaticamente após o registro
            return redirect('login')  # Redireciona para o login após registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Login de usuários
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/')  # Redireciona após login bem-sucedido
            else:
                return HttpResponse("Login inválido. Verifique suas credenciais.")
        else:
            return HttpResponse("Formulário inválido.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Logout do usuário
def logout(request):
    auth_logout(request)
    return redirect('login')  # Redireciona para a página de login após logout

# TABELA RESEARCH
def view_research(request):
    context = {'view_research': Research.objects.all()}
    return render(request, "research_table.html", context)

def form_research(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ResearchForm()
        else:
            research = Research.objects.get(pk=id)
            form = ResearchForm(instance=research)
        return render(request, "research_form.html", {'research_form': form})
    else:
        if id == 0:
            form = ResearchForm(request.POST)
        else:
            research = Research.objects.get(pk=id)
            form = ResearchForm(request.POST, instance=research)
        if form.is_valid():
            form.save()
        return redirect('/research/')

def delete_research(request, id):
    research = Research.objects.get(pk=id)
    research.delete()
    return redirect('/research/')

# TABELA RESEARCH GROUP
def view_researchGroup(request):
    context = {'view_researchGroup': ResearchGroup.objects.all()}
    return render(request, "researchGroup_table.html", context)

def form_researchGroup(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ResearchGroupForm()
        else:
            researchGroup = ResearchGroup.objects.get(pk=id)
            form = ResearchGroupForm(instance=researchGroup)
        return render(request, "researchGroup_form.html", {'researchGroup_form': form})
    else:
        if id == 0:
            form = ResearchGroupForm(request.POST)
        else:
            researchGroup = ResearchGroup.objects.get(pk=id)
            form = ResearchGroupForm(request.POST, instance=researchGroup)
        if form.is_valid():
            form.save()
        return redirect('/researchGroup/')

def delete_researchGroup(request, id):
    researchGroup = ResearchGroup.objects.get(pk=id)
    researchGroup.delete()
    return redirect('/researchGroup/')
