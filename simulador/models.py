from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


# ------------------------------------------------------- #
# CLASSE SERVIÇO                                          #
# ------------------------------------------------------- #
class servico(models.Model):
    desc_servico = models.CharField('Descrição', max_length=50, default='', blank=False, null=False)

    # para melhor visualizar no localhost\admin
    def __str__(self):
       return self.desc_servico

    # indica como desejamos que o nome de classe seja exibida no localhost/admin
    class Meta:
       verbose_name = 'servico'
       verbose_name_plural = 'servicos'
       # indica a ordem que desejamos que os dados sejam apresentados no local/admin (+ ascendente, - decrescente)
       ordering = ['desc_servico']


# ------------------------------------------------------- #
# CLASSE ITENS DO SERVIÇO                                 #
# ------------------------------------------------------- #
class itemservico(models.Model):
    desc_itemservico = models.CharField('Descrição', max_length=50, default='', blank=False, null=False)
    qtd_itemservico = models.IntegerField('Quantidade', default=1, blank=True, null=True)
    val_itemservico = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    val_recolhimentofundo = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    val_outros = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    val_totalitemservico = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    servico = models.ForeignKey(servico, default='', blank=True, null=True, on_delete=models.CASCADE)  # Chave estrangeira da Classe Serviço
    ind_selecionado = models.BooleanField(default=False)

    # para melhor visualizar no localhost\admin
    def __str__(self):
       return self.desc_itemservico

    def get_absolute_url_simulador_itens(self):
        return reverse("simulador_itens", kwargs={"id": self.id})

    # indica como desejamos que o nome de classe seja exibida no localhost/admin
    class Meta:
       verbose_name = 'itemservico'
       verbose_name_plural = 'itensservicos'
       # indica a ordem que desejamos que os dados sejam apresentados no local/admin (+ ascendente, - decrescente)
       ordering = ['desc_itemservico']


# ------------------------------------------------------- #
# CLASSE IMPOSTOS                                         #
# ------------------------------------------------------- #
class imposto(models.Model):
    desc_imposto = models.CharField('Descrição', max_length=50, default='', blank=False, null=False)
    val_outros   = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    perc_imposto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    # para melhor visualizar no localhost\admin
    def __str__(self):
       return self.desc_imposto

    # indica como desejamos que o nome de classe seja exibida no localhost/admin
    class Meta:
       verbose_name = 'imposto'
       verbose_name_plural = 'impostos'
       # indica a ordem que desejamos que os dados sejam apresentados no local/admin (+ ascendente, - decrescente)
       ordering = ['desc_imposto']
