from .models import *
import django_filters

class itemservicoFilter(django_filters.FilterSet):

    #dat_transacao = django_filters.DateFilter()
    #dat_inicial = django_filters.DateFilter(name='dat_transacao')#,lookup_type=('gte'))
    #dat_final = django_filters.DateFilter(name='dat_transacao')#,lookup_type=('lte'))

    #servico = django_filters.DateFromToRangeFilter()

    #self.form.fields['service_date'].fields[0].input_formats = ['%d-%m-%Y']
    #self.form.fields['service_date'].fields[-1].input_formats = ['%d-%m-%Y']


    #dat_transacao = django_filters.DateTimeFromToRangeFilter(
    #    widget=django_filters.widgets.RangeWidget(
    #        attrs={'class': 'datepicker'}
    #    )
    #)

    class Meta:
        model = itemservico
        fields = ['servico']

