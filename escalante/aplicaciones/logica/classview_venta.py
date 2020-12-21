from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import VentaForm
from .models import Venta, Lote

#Listar todas las Ventas
class VentaList(ListView):
    model = Venta
    template_name = 'listado_ventas.html'

#Crear nueva Venta
class VentaCreate(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'crear_venta.html'
    success_url = reverse_lazy('listado_ventas')
    #Modificar Lote vendido para que cambie su atributo exportado a TRUE
    def form_valid(self, form):
        if 'lote' in self.request.POST:
            lote = Lote.objects.get(id = self.request.POST['lote'])
            lote.exportado = True
            lote.save()
        return super().form_valid(form)

class VentaDelete(DeleteView):
        model = Venta
        success_url = reverse_lazy('listado_ventas')
        template_name = 'verificacion.html' #ventana verificacion para cuando borras un registro
