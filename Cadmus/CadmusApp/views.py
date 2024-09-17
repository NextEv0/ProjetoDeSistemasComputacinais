from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import *
from .forms import *

def home(request):
    return render(request, "index.html")

def base(request):
    return render(request, "base_generic.html")

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
        form = ContinentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('table/')
    
def delete_continent(request, id):
    continent = Continent.objects.get(pk=id)
    continent.delete()
    return redirect('/table/')

def form_country(request):
    form = CountryForm()
    return render(request, "tables_form.html", {'country_form':form})


#@login_required