from django.conf.urls import url
from django.urls import reverse
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.simulador_home, name='simulador_home'),  #localhost:8000

]

