from django.db import models
from django.utils import timezone

class Rolle(models.Model):

    relasjon = models.CharField(max_length=40)
    betaling = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.relasjon
        
class Leilighet(models.Model):

    leil = models.CharField(max_length=20)  
    kvadrat = models.IntegerField()
    
    
    def __str__(self):
        return self.leil        
    
class Person(models.Model):
    
    fnavn = models.CharField(max_length=40)
    enavn = models.CharField(max_length=60)
    telefon = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True, null=True)
    gateaddresse = models.CharField(max_length=40, blank=True)
    byaddresse = models.CharField(max_length=40, blank=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    roller = models.ManyToManyField(Rolle, blank=True,related_name= 'persons')
    leilighet=models.ManyToManyField(Leilighet, blank=True, related_name='leilig')

    def __str__(self):
        return "%s %s" % (self.fnavn, self.enavn)
 
    #a1, en instance av Rolle gir eks. a1.persons.all() alle personer
    # knyttet til denne rollen.
#
#   Mulig prosedyre for å finne styret med verv og ansvar:      
#   a = Person.object.filter(roller__relasjon__contains = 'sty')
#   for element in a:
#       c = element.roller.filter(relasjon__contain = 'ans')
#       b = element.roller.filter(relasjon__contain = 'sty')
#       element = styremedlem, b = styreverv, c = ansvar eller blank
#
    
         
   
# lookup i databasen eks:Person.objects.filter(roller__relasjon__startswith='styret')
# gir oss alle personer i styret. '

class Linker(models.Model):
    link = models.URLField(blank = True)
    navn = models.CharField(max_length=40)
    type = models.CharField(max_length=12, blank = True)

    
    def __str__(self):
        return "%s %s" % (self.navn, self.link)

class Kategori(models.Model):
    kat = models.CharField(max_length=40, default='medlemsinnlegg')   
    type = models.CharField(max_length=12, blank = True)
    logo = models.FileField(max_length=80, blank=True, null=True)
    
    def __str__(self):
        return self.kat
        
class Innlegg(models.Model):
    kategori = models.ForeignKey('bolig.Kategori', related_name='kats')
    title = models.CharField(max_length=60)
    tekst = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    tillatsvar = models.BooleanField(default=False)        

    def __str__(self):
        return self.title
        
class Kommentar(models.Model):
    post = models.ForeignKey('bolig.Innlegg', related_name='svar')
    author = models.CharField(max_length=80)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
           
    def __str__(self):
        return self.title    
