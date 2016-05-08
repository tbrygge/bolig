from django.contrib import admin

from .models import Person, Leilighet, Rolle, Linker, Kategori, Innlegg, Kommentar 

admin.site.register(Person)
admin.site.register(Leilighet)
admin.site.register(Rolle)
admin.site.register(Linker)
admin.site.register(Kategori)
admin.site.register(Innlegg)
admin.site.register(Kommentar)
# Register your models here.

site_title = 'Brygge-administrasjon'
