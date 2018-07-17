from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .models import *
from .forms import *
from .filters import itemservicoFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum


# Create your views here.

# ------------------------------------------------------------------------------------------------------------------ #
# Tela Inicial
# ------------------------------------------------------------------------------------------------------------------ #
def simulador_home(request):

    # -----> INICIO atualização dos valores <----- #

    # Somatório do Percentual de Recolhimento
    inst_imposto = imposto.objects.all().aggregate(Sum('perc_imposto'))
    var_percimposto = inst_imposto['perc_imposto__sum']

    # Somatório de outros valores
    inst_outros = imposto.objects.all().aggregate(Sum('val_outros'))
    var_valoutros = inst_outros['val_outros__sum']

    # Atualiza os impostos/outros nos itens do servico
    #itemservico.objects.all().update(val_recolhimentofundo=var_percimposto)
    #itemservico.objects.all().update(val_outros=var_valoutros)

    # Atualiza o valor total do item do serviço
    instance_itemservico = itemservico.objects.all()
    for item in instance_itemservico:
        # Pega os valores
        var_valitemservico = item.val_itemservico
        var_valoutros = item.val_outros
        var_valrecolhimentofundo = item.val_recolhimentofundo
        # Calcula o imposto
        var_imposto = var_valitemservico * var_valrecolhimentofundo/100
        # Calcula o valor total
        var_valtotal = var_valitemservico + var_valoutros + var_imposto
        # Atualiza o valor total
        item.val_totalitemservico = var_valtotal
        item.save()

    # -----> FIM atualização dos valores <----- #

    form = itemservicoForm(request.POST or None)

    # Seleciona a lista para ser exibida no grid
    instancia_item_list = itemservico.objects.all().order_by('desc_itemservico')
    instancia_item_filter = itemservicoFilter(request.GET, queryset=instancia_item_list)

    paginator = Paginator(instancia_item_filter.qs, 100)
    page = request.GET.get('page')

    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        response = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last pages of results
        response = paginator.page(paginator.num_pages)

    context = {
        "filter": instancia_item_filter,
        "response": response,
        "form": form
    }
    return render(request, "simulador/itemservico.html", context)



# Videos interessantes:
# https: // www.youtube.com / watch?v = nEAi0Z9MnDg
# many to many : https://www.youtube.com/watch?v=bFhuOULgKDs&index=55&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj
# ver: https://stackoverflow.com/questions/9602804/adding-extra-info-in-form-field-and-use-it-while-rendering-django-template?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
