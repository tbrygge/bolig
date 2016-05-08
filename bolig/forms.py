from django import forms
from .models import Innlegg, Kommentar, Kategori, Person



class InnleggForm(forms.ModelForm):
    
    class Meta:
        
        model = Innlegg     
       
        fields = ('kategori','title','tekst')            
        
        def __init__(self, *args, **kwargs):             
            super(self, InnleggForm).__init__(*args, **kwargs)
            # dette er pseudo kode men henter all informasjon
            # deretter settes kategorifeltet til valg av kategoriobjekter fra databasen
            
            self.fields['kategori'] = forms.ChoiceField(choices = Kategori.objects.all(),initial='medlemsinnlegg')
            
class KommentarForm(forms.ModelForm):

    class Meta:
        model = Kommentar
        fields = ('author', 'text')
        
class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('fnavn', 'enavn', 'telefon', 'email', 'gateaddresse', 'byaddresse')
        
class MynyForm(forms.ModelForm):
    
    class Meta:
        
        model = Innlegg     
       
        fields = ('kategori','title','tekst')            
        exclude = ('kategori',)
        
        def __init__(self, *args, **kwargs):
                          
            super(self, MynyForm).__init__(*args, **kwargs)
            # dette er pseudo kode men henter all informasjon
            # deretter settes kategorifeltet til valg av kategoriobjekter fra databasen
           
