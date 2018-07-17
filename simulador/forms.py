# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.forms import ModelForm
from .models import servico, itemservico


class servicoForm(forms.ModelForm):

    desc_servico = forms.ModelChoiceField(queryset=servico.objects.all().order_by('desc_servico'), empty_label="Serviço")

    class Meta:
        model = servico
        fields = (
                    'desc_servico',
                  )


class itemservicoForm(forms.ModelForm):

    servico = forms.ModelChoiceField(queryset=servico.objects.all().order_by('desc_servico'), empty_label="Serviço")
    #ind_selecionado = forms.BooleanField( widget=forms.RadioSelect)

    class Meta:
        model = itemservico
        fields = (
                    'servico',
                  )


