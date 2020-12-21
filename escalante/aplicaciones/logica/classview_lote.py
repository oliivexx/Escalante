from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import LoteForm
from .models import Lote

#Listar todos los Lotes que no esten exportados
class LoteList(ListView):
    model = Lote
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        lotes = Lote.objects.filter(exportado = False)
        return render(request, 'index.html', locals())

#Crear nuevo Lote
class LoteCreate(CreateView):
    model = Lote
    form_class = LoteForm
    template_name = 'crear_lote.html'
    success_url = reverse_lazy('index')

#Modificar un Lote
class LoteUpdate(UpdateView):
    model = Lote
    form_class = LoteForm
    template_name = 'crear_lote.html'
    success_url = reverse_lazy('index')
    
#Eliminar Lote
class LoteDelete(DeleteView):
    model = Lote
    success_url = reverse_lazy('index')
    template_name = 'verificacion.html' #ventana verificacion para cuando borras un registro
