from xml.dom.minidom import Document
from django.shortcuts import redirect, render
from .models import Usuario

# Create your views here.
def index(request):
    return render(request,'usuarios/index.html')

def usuarios(request):
    
    #Salvar usuarios
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('tNome')
    novo_usuario.telefone = request.POST.get('tCel')
    novo_usuario.email = request.POST.get('tEmail')
    novo_usuario.save()
    #Exibir usuarios
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Retornar os usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)

def lista_usuarios(request):
    #Exibir usuarios
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Retornar os usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)

def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'usuarios/editar.html', {"usuario": usuario})

def update_usuarios(request, id):
    # Aqui é o que vem da tela 
    nome = request.POST.get("tNome")
    telefone = request.POST.get("tCel")
    email = request.POST.get("tEmail")
    # aqui é o que é carregado do banco
    usuario = Usuario.objects.get(id=id)
    usuario.nome = nome
    usuario.telefone = telefone
    usuario.email = email
    usuario.save()
    return redirect(lista_usuarios)

def deletar_usuarios(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect(lista_usuarios)
    
