from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Foto


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'exibir_miniatura', 'titulo', 'categoria', 'created_at', 'updated_at')
    readonly_fields = ('visualizar_foto_grande',)

    def exibir_miniatura(self, obj):
        if obj.imagem:
            return mark_safe(f'<img src="{obj.imagem.url}" width="50" style="border-radius: 5px;" />')
        return "Sem imagem"
     
    exibir_miniatura.short_description = 'Miniatura'

    def visualizar_foto_grande(self, obj):
        if obj.imagem:
            return mark_safe(f'<img src="{obj.imagem.url}" width="300" />')
        return "Sem imagem"

    visualizar_foto_grande.short_description = 'Visualização'
