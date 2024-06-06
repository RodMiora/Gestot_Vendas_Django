from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




def redirect_to_login(request):
    return redirect('/usuarios/login/')



def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        users = User.objects.filter(username=username)
        
        if users.exists():
            messages.add_message(request, constants.ERROR, "Já existe um usuário com esse nome")
            return redirect('/usuarios/cadastro')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, "A senha e o confirmar senha devem ser iguais")
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, "A senha deve ter mais de 6 dígitos")
            return redirect('/usuarios/cadastro')
        
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )
            user.is_active = True  # Certifique-se de que o usuário está ativo
            user.save()
        
            messages.add_message(request, constants.SUCCESS, "Usuário criado com sucesso!")
            return redirect('/usuarios/login')
        except:
            print('Erro 4')
            return redirect('/usuarios/cadastro')

  
def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')  # Use 'password' para acessar o campo de senha

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')  # Redirecionar para a página de dashboard

        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos!')
        return redirect('/usuarios/login')


def sair(request):
    auth.logout(request)
    return redirect('/usuarios/login')
