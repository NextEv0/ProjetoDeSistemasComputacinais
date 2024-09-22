from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import *
from .forms import *
from django.db import connection

def home(request):
    return render(request, "index.html")

def base(request):
    return render(request, "base_generic.html")

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

def form_country(request):
    form = CountryForm()
    return render(request, "tables_form.html", {'country_form': form})

# Funções para CRUD geral

# Função para listar as tabelas do banco de dados
def list_tables():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema='public'
        """)
        tables = cursor.fetchall()
    return [table[0] for table in tables]

# Função para exibir a página de escolha de tabela
def choose_table(request):
    tables = list_tables()
    return render(request, 'choose_table.html', {'tables': tables})

# Função para exibir os dados da tabela escolhida
def view_table_data(request, table_name):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 100")
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
    
    return render(request, 'table_data.html', {'rows': rows, 'colnames': colnames, 'table_name': table_name})

# Função para criar um novo registro na tabela escolhida
def create_record(request, table_name):
    if request.method == "POST":
        columns = request.POST.getlist('columns')
        values = request.POST.getlist('values')
        
        columns_str = ', '.join(columns)
        values_str = ', '.join([f"'{value}'" for value in values])

        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})")
        
        return redirect('view_table_data', table_name=table_name)
    
    return render(request, 'create_record.html', {'table_name': table_name})
