
from django.apps import apps

#NB! NB!
# kan ikke importere models direkte fordi Django sjekker i flere stadier og gir feil
# fordi importen sjekkes før modellene er installerte. Dette virker fordi man henter 
# model data etter at all setup er ferdig...
from django import template
#from bolig.models import Rolle


register = template.Library()

@register.inclusion_tag('bolig/mytags/under_menu.html')
def under_menu():
    z = apps.get_model('bolig','Linker')  
    return {'undermenu': z.objects.filter(type__contains='type 1')}
    
@register.inclusion_tag('bolig/mytags/under_menu2.html')
def under_menu2():
    z = apps.get_model('bolig', 'Kategori')      
    return {'undermenu2': z.objects.all()}    

@register.inclusion_tag('bolig/mytags/under_menu3.html')
def under_menu3(navn):
    z = apps.get_model('bolig', 'Leilighet')
    p = z.objects.get(leil__contains= navn)
    return {'undermenu3': p.leilig.all()} # alle personene tilknyttet leiligheten.
     