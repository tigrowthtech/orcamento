from django.contrib import admin
from .models import servico, itemservico

# Register your models here.


class servicoModelAdmin(admin.ModelAdmin):
    # campos que serão listados no localhost:8000/admin
    list_display = ["desc_servico"]
    # ao clicar no campo 'dat_alteracao' vai direto para o registro
    list_display_links = ["desc_servico"]
    # é exibida o filtro no módulo admin
    list_filter = ["desc_servico"]
    # pesquisa pelo campo no admin
    search_fields = [ "desc_servico"]
    save_on_top = True
    class Meta:
        model = servico


class itemservicoModelAdmin(admin.ModelAdmin):
    # campos que serão listados no localhost:8000/admin
    list_display = ["desc_itemservico"]
    # ao clicar no campo 'dat_alteracao' vai direto para o registro
    list_display_links = ["desc_itemservico"]
    # é exibida o filtro no módulo admin
    list_filter = ["desc_itemservico"]
    # pesquisa pelo campo no admin
    search_fields = [ "desc_itemservico"]
    save_on_top = True
    class Meta:
        model = itemservico

# Objetiva exibir essas tabelas no localhost:8000/admin
admin.site.register(servico, servicoModelAdmin)
admin.site.register(itemservico, itemservicoModelAdmin)