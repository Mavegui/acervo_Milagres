from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Foto

def index(request):
    categoria_select = request.GET.get('categoria')
    
    categorias_validas = {valor for valor, _ in Foto.CATEGORIAS_CHOICES}
    if categoria_select and categoria_select not in categorias_validas:
        messages.error(request, "A categoria selecionada não existe.")
        return redirect('index')

    fotos_list = Foto.objects.all()
    if categoria_select:
        fotos_list = fotos_list.filter(categoria=categoria_select)
    
    fotos_list = fotos_list.order_by('-id')

    paginator = Paginator(fotos_list,8)
    page_number = request.GET.get('page')
    fotos = paginator.get_page(page_number)

    context = {
        'fotos': fotos,
        'categorias': Foto.CATEGORIAS_CHOICES,
        'categoria_ativa': categoria_select,
    }

    return render(request, 'acervo/index.html', context)

def sobre(request):
    return render(request, 'acervo/sobre.html')