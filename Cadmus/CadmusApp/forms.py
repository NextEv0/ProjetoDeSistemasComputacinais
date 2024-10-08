from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

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

class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = ['research_groupid', 
                  'license_rights', 
                  'collection_code', 
                  'ocurrenceid', 
                  'basis_of_record', 
                  'ocurrence_status', 
                  'preparations', 
                  'event_date', 
                  'event_remarks', 
                  'publishing_country', 
                  'localization',]

    event_date = forms.DateField(
    localize=True,
    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
)

    def __init__(self, *args, **kwargs):
        super(ResearchForm, self).__init__(*args, **kwargs)
        self.fields['localization'].empty_label = ""
        self.fields['publishing_country'].empty_label = ""
        self.fields['research_groupid'].empty_label = ""
        self.fields['license_rights'].empty_label = ""
        

class ResearchGroupForm(forms.ModelForm):
    class Meta:
        model = ResearchGroup
        fields = '__all__'
        

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

