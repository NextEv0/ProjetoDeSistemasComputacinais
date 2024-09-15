from django import forms
from .models import AnimalEntry

class AnimalEntryForm(forms.ModelForm):
    class Meta:
        model = AnimalEntry
        fields = ['nome', 'especie', 'idade']  # Campos do modelo que deseja incluir no formulário
