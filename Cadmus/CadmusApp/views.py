from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import *
from .forms import *

def home(request):
    return render(request, "index.html")

#TABELA CONTINENTE
def view_continent(request):
    context = {'view_continent':Continent.objects.all()}
    return render(request, "tables_copy.html", context)

def form_continent(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ContinentForm()
        else:
            continent = Continent.objects.get(pk=id)
            form = ContinentForm(instance=continent)
        return render(request, "tables_form.html", {'continent_form':form})
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

#TABELA RESEARCH
def view_research(request):
    context = {'view_research':Research.objects.all()}
    return render(request, "research_table.html", context)

def form_research(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ResearchForm()
        else:
            research = Research.objects.get(pk=id)
            form = ResearchForm(instance=research)
        return render(request, "research_form.html", {'research_form':form})
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

#TABELA RESEARCH GROUP
def view_researchGroup(request):
    context = {'view_researchGroup':ResearchGroup.objects.all()}
    return render(request, "researchGroup_table.html", context)

def form_researchGroup(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ResearchGroupForm()
        else:
            researchGroup = ResearchGroup.objects.get(pk=id)
            form = ResearchGroupForm(instance=researchGroup)
        return render(request, "researchGroup_form.html", {'researchGroup_form':form})
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

def form_country(request):
    form = CountryForm()
    return render(request, "research_form.html", {'country_form':form})


#@login_required