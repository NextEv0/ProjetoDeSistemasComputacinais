from django import forms
from .models import *

class ContinentForm(forms.ModelForm):
    class Meta:
        model = Continent
        fields = '__all__'

        labels = {
        'continent_name' : 'Nome do Continente',
        }

        widgets ={
        "continent_name" : forms.TextInput(attrs={"placeholder":"algum lugar ai"}),
        }

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        
        labels={
            'country_name' : 'Nome do país',
            'continent' : 'Continente que pertence',
            'level0gid' : 'Sigla do país',
        }
    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)
        self.fields['continent'].empty_label = "Selecione o continente"

