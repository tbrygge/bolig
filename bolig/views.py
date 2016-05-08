
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template.context_processors import request
from django import forms
from .models import Person, Rolle, Leilighet, Innlegg, Kategori, Kommentar
from .forms import InnleggForm, KommentarForm, PersonForm, MynyForm

import os



def vis_styret(request):
        	
    sok =['t leder', 'nestl','t medlem','vara']
    styret = [] 
    rolle = []
    ansvar = []
    leilig = []
    for element in sok:
        styret += Person.objects.filter(roller__relasjon__contains = element)
    for b in styret:
        rolle += b.roller.filter(relasjon__contains = 'sty')
        a = b.roller.filter(relasjon__contains =   'ans') 
        if a:
            ansvar += a
        else:
            ansvar += ' '
#
        leilig += [finn_flere(b.leilighet.all(), 'leil')] # leilig er en streng med leiligheter mot person i styret.
    valg = Person.objects.filter(roller__relasjon__contains = 'valg')
    leip = []
    for a in valg:
        leip += [finn_flere(a.leilighet.all(), 'leil')]
                
    mylist = zip(styret, rolle, ansvar, leilig)
    vlist = zip(valg, leip)
    
    # Det over er leilighetene. Vi prosesserer også referatene her.
    # Her putter vi på referater for å presenteres på samme side som styret
    # De passer inn her.
    
    path = os.path.dirname(os.path.abspath(__file__))
    mypath = os.path.join(path,'static\docs')
    
    a = os.listdir(mypath)    # get motereferater
    mypath = mypath + '\\'
    moter = []
    mott = []
    styref = []
    styrt = []
    for item in a:
        b = ''.join([i for i in item if i.isdigit()])
        if len(b) >= 5:       
            styref.append(b[4:] + b[2:4] + b[0:2] + item)
        elif len(b) >= 3:
            moter.append(b + item)
    styref.sort(reverse = True)
    moter.sort(reverse = True)
    for i in range(len(styref)):
        styrt.append('Referat ' + styref[i][4:6] +'.' + styref[i][2:4] + '.' + styref[i][0:2])
        styref[i] = 'static/docs/' + styref[i][6:]        
    for i in range(len(moter)):
        mott.append('Aarsmote ' + moter[i][:4])
        moter[i] = 'static/docs/' + moter[i][4:]
    
    styreref = zip(styrt, styref)
    amoter = zip(mott, moter)  
    domene2 = request.build_absolute_uri('/')
    
    context= {
        'mylist': mylist,
        'vlist' : vlist,
        'styreref': styreref,
        'amoter' : amoter,
        'domene2' : domene2,
    }
        
    return render(request, 'bolig/list_styret.html', context)
   
def finn_flere(bo, felt):      # Fyller ut tekstlisten med blanke eller objektet for listesamsvar
#        a = bo.leilighet.all()
    nr = ' '
    if bo:
        nr =''
        b = ''
    for c in bo:
            nr += b + getattr(c,felt)
            b = ','
    return nr   
# Create your views here.
#def post_detail(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    return render(request, 'blog/post_detail.html', {'post': post})

#@login_required    
#def post_new(request):
#   if request.method == "POST":
#        form = PostForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user           
#            post.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = PostForm()
#        return render(request, 'blog/post_edit.html', {'form': form})

def list_bolig(request):

    class Teier:
        def __init__self():
            self.app = ''
            self.boi = True
            self.name = []
            self.mailtel = []
        
    a3 = Leilighet.objects.filter(leil__contains = 'A3').order_by('-leil')
    a2 = Leilighet.objects.filter(leil__contains = 'A2').order_by('-leil')
    a1 = Leilighet.objects.filter(leil__contains = 'A1').order_by('-leil')


    b2 = Leilighet.objects.filter(leil__contains = 'B2').order_by('leil') | Leilighet.objects.filter(leil__contains='C2').order_by('leil')
    b1 = Leilighet.objects.filter(leil__contains = 'B1').order_by('leil') | Leilighet.objects.filter(leil__contains='C1').order_by('leil')
    
    flag = True

    blokk = [Teier()]
    teller = a3, a2, a1, b2, b1  # alle leiligheter i riktig rekkefølgere
    for i in teller:
        for item in i:
            b = Teier()
            b.app = item.leil
            b.boi = True           # sett eier bor i bolig som default
            b.name = []
            b.mailtel = []
            c = item.leilig.all()  # alle personer tilknyttet leilighet
            for d in c:
                if d.roller.filter(relasjon__contains = 'utleier'): # utleier ?
                    b.boi = False                                   # ja, fjern flagg
                if d.roller.filter(relasjon__contains='eiger'):     # Hent eierdata
                    b.name += [d.fnavn +' '+ d.enavn +'| ' + d.telefon]
                    b.mailtel += [d.email]

            if flag:
                blokk[0] = b                                    # sett første instance
                flag = False
            else:    
                blokk.append(b)                                 # siden legges nye title               
            del b
 
    context= {
        
        'blokk' : blokk
        
    }
    
    return render(request, 'bolig/list_bolig.html', context)

#    
def start_opp(request): 
    return render(request, 'bolig/start_opp.html')
#    
# det under er flyttet til vis_styret. Passer med referater der...
#    
def vis_det(request, fref):    
#    
#    
    tekst = fref
    context = {
        'tekst' : tekst,
    }
    return render(request,'bolig/vis_det.html', context)
    
def vis_innlegg(request, hva):
#
#  denne viser poster i innlegg. 
#  hva inneholder filterverdi om noen
#
    logo =[]
    if hva != 'alle':
        innlegg= Innlegg.objects.filter(kategori__kat= hva).order_by('-created_date') #nyeste først       
    else:
        innlegg= Innlegg.objects.all().order_by('-created_date') #hent alle
    for item in innlegg:
        katt = Kategori.objects.get(kat=item.kategori) # plukk ut kategori       
        logo.append( katt.logo) # sett inn i array     
    pakk = zip(innlegg,logo) 
    context = {       
        'pakk' : pakk,
     }
        
    return render(request, 'bolig/vis_alle.html', context)
        
    
# 
# Vi plukker opp en post for detailvisning. Herfra legger vi mulighet for editering
def get_user_kategori(user):
    liste = {'eiere': 'medlemsinnlegg', 'styret': 'styret', 'arbeid': 'vaktmester'}    
    for key in liste:
        if user.groups.filter(name__contains=key):    
            return Kategori.objects.get(kat__contains=liste[key])
    return False    
    
def innlegg_detail(request, pk):
    innlegg = get_object_or_404(Innlegg, pk=pk)
    return render(request, 'bolig/innlegg_detail.html', {'innlegg': innlegg})

@login_required        
def innlegg_edit(request, pk):
    innlegg = get_object_or_404(Innlegg, pk=pk)
    item = get_user_kategori(user=request.user)
    if request.method == "POST":
        if item:
            form = MynyForm(request.POST, instance = innlegg)
        else:    
            form = InnleggForm(request.POST, instance=innlegg)
        if form.is_valid():
            innlegg = form.save(commit=False)        
            innlegg.save()
            return redirect('innlegg_detail', pk=innlegg.pk)            
    else:
        if item:
            form = MynyForm(instance=innlegg)
        else:    
            form = InnleggForm(instance=innlegg)
    return render(request, 'bolig/innlegg_edit.html', {'form': form})
    
@login_required
def innlegg_fjern(request, pk):
    innlegg = get_object_or_404(Innlegg, pk=pk)
    innlegg.delete()
    return redirect('bolig.views.vis_innlegg', 'alle')

def nytt_innlegg(request):
    item = get_user_kategori(user=request.user)
    user = request.user
    if request.method == "POST":
        if item:
            form = MynyForm(request.POST)            
        else:
            form = InnleggForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if item:
                post.kategori = item   
            post.save()
            return redirect('innlegg_detail', pk=post.pk)
    else:
        if item:
            form = MynyForm()
        else:    
            form = InnleggForm()
                  
        return render(request, 'bolig/innlegg_edit.html', {'form': form })    

def ny_kommentar_til_innlegg(request, pk):
    innlegg = get_object_or_404(Innlegg, pk=pk)
    if request.method == "POST":
        form = KommentarForm(request.POST)
        if form.is_valid():
            kommentar = form.save(commit=False)
            kommentar.post = innlegg
            kommentar.save()
            return redirect('bolig.views.innlegg_detail', pk=innlegg.pk)
    else:
        form = KommentarForm()
    return render(request, 'bolig/ny_kommentar_til_innlegg.html', {'form': form}) 

@login_required
def kommentar_fjern(request, pk):
    kommentar = get_object_or_404(Kommentar, pk=pk)
    post_pk = kommentar.post.pk
    kommentar.delete()
    return redirect('bolig.views.innlegg_detail', pk=post_pk)

@login_required        
def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)            
            person.save()
            next = request.GET.get('next', None)
            if next:
                return redirect(next)
            return redirect('list_bolig')            
    else:
        form = PersonForm(instance=person)
    return render(request, 'bolig/person_edit.html', {'form': form})    

