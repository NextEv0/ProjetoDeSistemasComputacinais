from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AnimalEntry
from .forms import AnimalEntryForm

@login_required
def animal_list(request):
    entries = AnimalEntry.objects.filter(created_by=request.user)
    return render(request, 'cadmusapp/animal_list.html', {'entries': entries})

@login_required
def animal_create(request):
    if request.method == 'POST':
        form = AnimalEntryForm(request.POST)
        if form.is_valid():
            animal_entry = form.save(commit=False)
            animal_entry.created_by = request.user
            animal_entry.save()
            return redirect('animal_list')
    else:
        form = AnimalEntryForm()
    return render(request, 'cadmusapp/animal_form.html', {'form': form})

@login_required
def animal_update(request, pk):
    entry = get_object_or_404(AnimalEntry, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = AnimalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalEntryForm(instance=entry)
    return render(request, 'cadmusapp/animal_form.html', {'form': form})

@login_required
def animal_delete(request, pk):
    entry = get_object_or_404(AnimalEntry, pk=pk, created_by=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('animal_list')
    return render(request, 'cadmusapp/animal_confirm_delete.html', {'entry': entry})
