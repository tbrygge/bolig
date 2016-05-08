from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.start_opp, name='start_opp'),   
    url(r'^vis_styret/$', views.vis_styret, name='vis_styret'),    
    url(r'^list_bolig/$', views.list_bolig, name='list_bolig'),
    url(r'^vis_innlegg/(?P<hva>[\w\ ]+)/$', views.vis_innlegg, name='vis_innlegg'),
    url(r'^nytt_innlegg/$', views.nytt_innlegg, name='nytt_innlegg'),
    url(r'^innlegg_detail/(?P<pk>\d+)/$', views.innlegg_detail, name='innlegg_detail'),
    url(r'^innlegg_edit/(?P<pk>\d+)/$', views.innlegg_edit, name='innlegg_edit'),
    url(r'^innlegg_fjern/(?P<pk>\d+)/$', views.innlegg_fjern, name='innlegg_fjern'),
    url(r'^ny_kommentar_til_innlegg/(?P<pk>\d+)/$', views.ny_kommentar_til_innlegg, name='ny_kommentar_til_innlegg'),
    url(r'^kommentar/(?P<pk>\d+)/fjern/$', views.kommentar_fjern, name='kommentar_fjern'),
    url(r'^person_edit/(?P<pk>\d+)/$', views.person_edit, name='person_edit'),
    url(r'^vis_det/(?P<fref>[.:\\//\w-]+)/$', views.vis_det, name='vis_det'),

]
# regex r = raw '^vis_det/(?P<arg>[\w\ ]+)/$',
# søker etter vis_det i views.<arg> er argument og siles
# etter \w\ alle bokstaver med -.. osv. \' ' tillater white space
# 