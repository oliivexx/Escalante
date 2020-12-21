from django.contrib import admin
from .models import Lote, Cliente, Factura, Venta

admin.site.register(Lote)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(Venta)
# Register your models here.
