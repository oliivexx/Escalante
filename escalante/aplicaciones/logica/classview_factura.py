from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .forms import FacturaForm
from .models import *
from datetime import datetime

#Listar todas las Facturas
class FacturaList(ListView):
    model = Factura
    template_name = 'listado_facturas.html'

#Crear nueva Factura
class FacturaCreate(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'crear_factura.html'
    success_url = reverse_lazy('listado_facturas')

#Eliminar Factura
class FacturaDelete(DeleteView):
        model = Factura
        success_url = reverse_lazy('listado_facturas')
        template_name = 'verificacion.html' #ventana verificacion para cuando borras un registro
