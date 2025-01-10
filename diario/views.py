from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Diario
from datetime import datetime, timedelta

def home(request):
    textos = Diario.objects.all().order_by('create_at')[:3]
    pessoas = Pessoa.objects.all()
    qtds = []
    nomes = [pessoa.nome for pessoa in pessoas]
    for pessoa in pessoas:
        qtd = Diario.objects.filter(pessoas=pessoa).count()
        qtds.append(qtd)
    
    return render(request, 'home.html', {'textos': textos, 'nomes': nomes, 'qtds': qtds}) 

def escrever(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        return render(request, 'escrever.html', {'pessoas':pessoas})
    
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')

        # Validação no servidor: Verifica se 'titulo' e 'texto' estão preenchidos
        if not titulo.strip() or not texto.strip():
            # Se algum campo obrigatório estiver vazio, redireciona o usuário de volta para a página de escrever
            return render(request, 'escrever.html', {
                'erro': 'Título e Texto são obrigatórios.',  # Mensagem de erro
                'pessoas': Pessoa.objects.all()  # Recarrega a lista de pessoas no formulário
            })
        
        # Se a validação passar, o diário será salvo
        diario = Diario(
            titulo=titulo,
            texto=texto
        )
        diario.set_tags(tags)
        diario.save()

        for i in pessoas:
            pessoa = Pessoa.objects.get(id=i)
            diario.pessoas.add(pessoa)

        diario.save()
        return redirect('escrever')
    
def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'pessoa.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')

        # Validação para garantir que o nome não está vazio
        if not nome.strip():
            return render(request, 'pessoa.html', {
                'erro': 'O nome é obrigatório.'  # Mensagem de erro se o nome estiver vazio
            })

        pessoa = Pessoa(
            nome=nome,
            foto=foto
        )
        pessoa.save()
        return redirect('escrever')
    
def dia(request):
    data = request.GET.get('data')

    # Validação para garantir que a data está presente
    if not data:
        return render(request, 'dia.html', {'erro': 'A data é obrigatória.'})

    try:
        # Tentativa de conversão da data para o formato adequado
        data_formatada = datetime.strptime(data, '%Y-%m-%d')
    except ValueError:
        return render(request, 'dia.html', {'erro': 'Formato de data inválido. Utilize o formato YYYY-MM-DD.'})
    
    # Filtra os diários para o dia selecionado
    diarios = Diario.objects.filter(create_at__gte=data_formatada).filter(create_at__lte=data_formatada + timedelta(days=1))

    return render(request, 'dia.html', {'diarios': diarios, 'total': diarios.count(), 'data': data})

def excluir_dia(request):
    dia = datetime.strptime(request.GET.get('data'), '%Y-%m-%d')
    diarios = Diario.objects.filter(create_at__gte=dia).filter(create_at__lte=dia + timedelta(days=1))
    diarios.delete()
    return redirect('escrever')
