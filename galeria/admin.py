from django.contrib import admin

from galeria.models import Fotografia
from galeria.models import Carro


class ListandoFotografias(admin.ModelAdmin):
    list_display = (all_fields := [field.name for field in Fotografia._meta.fields]);
    list_display_links = ('id', 'nome')
    search_fields = ['nome']
    list_filter = ['categoria']
    list_editable = ('publicada',)
    list_per_page = 10
        
class ListandoCarros(admin.ModelAdmin):
    list_display = (all_fields := [field.name for field in Carro._meta.fields]);
    list_display_links = ('id', 'marca')
    search_fields = ['marca']
    
admin.site.register(Fotografia, ListandoFotografias)
admin.site.register(Carro, ListandoCarros)