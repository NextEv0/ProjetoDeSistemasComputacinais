from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import *
from .forms import *
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import status, generics
from CadmusApp.models import NoteModel
from CadmusApp.serializers import NoteSerializer, ResearchSerializer
import math
from datetime import datetime


class NoteDetail(generics.GenericAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer

    def get_note(self, pk):
        try:
            return NoteModel.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        note = self.get_note(pk=pk)
        if note == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(note)
        return Response({"status": "success", "data": {"note": serializer.data}})

    def patch(self, request, pk):
        note = self.get_note(pk)
        if note == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = self.get_note(pk)
        if note == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Notes(generics.GenericAPIView):
    serializer_class = NoteSerializer
    queryset = NoteModel.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        notes = NoteModel.objects.all()
        total_notes = notes.count()
        if search_param:
            notes = notes.filter(title__icontains=search_param)
        serializer = self.serializer_class(notes[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_notes,
            "page": page_num,
            "last_page": math.ceil(total_notes / limit_num),
            "notes": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# View da página inicial
def home(request):
    return render(request, "index.html")

# View da página base
def base(request):
    return render(request, "base_generic.html")

# View para exibir continentes
def view_continent(request):
    context = {'view_continent': Continent.objects.all()}
    return render(request, "tables_copy.html", context)

# View para criar ou editar continentes
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
    
# View para deletar continentes
def delete_continent(request, id):
    continent = Continent.objects.get(pk=id)
    continent.delete()
    return redirect('/table/')

# View para adicionar país (country)
def form_country(request):
    form = CountryForm()
    return render(request, "tables_form.html", {'country_form': form})

# View para listar tabelas do banco de dados
def list_tables():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema='public'
        """)
        tables = cursor.fetchall()
    return [table[0] for table in tables]

# View para exibir a página de escolha de tabela
def choose_table(request):
    tables = list_tables()
    return render(request, 'choose_table.html', {'tables': tables})

# View para exibir os dados da tabela escolhida
def view_table_data(request, table_name):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 100")
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
    
    return render(request, 'table_data.html', {'rows': rows, 'colnames': colnames, 'table_name': table_name})

# View para criar um novo registro na tabela escolhida
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

# View para registro de novos usuários
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class ResearchDetail(generics.GenericAPIView):
    queryset = Research.objects.all()
    serializer_class = NoteSerializer

    def get_note(self, pk):
        print(pk)
        try:
            return Research.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk, *args, **kwargs):
        try:
            research = Research.objects.get(pk=pk)
            serializer = ResearchSerializer(research)
            return Response(serializer.data)
        except Research.DoesNotExist:
            return Response({
                "status": "fail",
                "message": f"Research with Id: {pk} not found"
            }, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk, *args, **kwargs):
        research = self.get_object(pk)
        serializer = ResearchSerializer(research, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        note = self.get_note(pk)
        if note == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Research(generics.GenericAPIView):
    serializer_class = NoteSerializer
    queryset = Research.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        notes = Research.objects.all()
        total_notes = notes.count()
        if search_param:
            notes = notes.filter(title__icontains=search_param)
        serializer = self.serializer_class(notes[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_notes,
            "page": page_num,
            "last_page": math.ceil(total_notes / limit_num),
            "notes": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
