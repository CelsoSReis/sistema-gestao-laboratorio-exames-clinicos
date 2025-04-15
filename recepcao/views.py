from django.shortcuts import render, redirect, get_object_or_404
from .models import Convenio

def convenio_list(request):
    convenios = Convenio.objects.all()
    return render(request, 'recepcao/convenio_list.html', {'convenios': convenios})

def convenio_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        site = request.POST.get('site')
        ativo = bool(request.POST.get('ativo'))

        Convenio.objects.create(
            nome=nome,
            cnpj=cnpj,
            telefone=telefone,
            email=email,
            site=site,
            ativo=ativo
        )
        return redirect('convenio_list')
    return render(request, 'recepcao/convenio_form.html')

def convenio_update(request, pk):
    convenio = get_object_or_404(Convenio, pk=pk)
    if request.method == 'POST':
        convenio.nome = request.POST.get('nome')
        convenio.cnpj = request.POST.get('cnpj')
        convenio.telefone = request.POST.get('telefone')
        convenio.email = request.POST.get('email')
        convenio.site = request.POST.get('site')
        convenio.ativo = bool(request.POST.get('ativo'))
        convenio.save()
        return redirect('convenio_list')
    return render(request, 'recepcao/convenio_form.html', {'convenio': convenio})

def convenio_delete(request, pk):
    convenio = get_object_or_404(Convenio, pk=pk)
    if request.method == 'POST':
        convenio.delete()
        return redirect('convenio_list')
    return render(request, 'recepcao/convenio_confirm_delete.html', {'convenio': convenio})
