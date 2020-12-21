from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import ClienteForm
from .models import Cliente

#Listar todos los Clientes
class ClienteList(ListView):
    model = Cliente
    template_name = 'listado_clientes.html'

#Crear Nuevo Cliente
class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'crear_cliente.html'
    success_url = reverse_lazy('listado_clientes')

#Modificar Cliente
class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'crear_cliente.html'
    success_url = reverse_lazy('listado_clientes')

#Eliminar Cliente
class ClienteDelete(DeleteView):
        model = Cliente
        success_url = reverse_lazy('listado_clientes')
        template_name = 'verificacion.html' #ventana verificacion para cuando borras un registro
