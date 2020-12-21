from django import forms
from .models import Lote, Cliente, Venta, Factura

#Archivo para la generacion automática de formularios de Django para crear nuevos objetos
class LoteForm(forms.ModelForm):
    class Meta:
        model = Lote
        fields = ('codigo', 'descripcion', 'palets',)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields= ('nombre', 'direccion', 'poblacion', 'provincia', 'cp',)

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ('lote', 'cliente')

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('cliente', 'fecha', )
