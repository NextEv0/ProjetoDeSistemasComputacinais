from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "index.html")

def crud(request):
    return render(request, "tables.html")

#@login_required