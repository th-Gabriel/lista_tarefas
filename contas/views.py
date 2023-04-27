from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import HttpResponse

# Create your views here.
def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    

def cadastro_page(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    if request.method == 'POST':
        try:
            user = User(
                first_name = request.POST['nome'],
            last_name = request.POST['sobrenome'],
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password']
            )

            user.save()
            Token.objects.create(user=user)
            return HttpResponse(f'Usuário {user.username} salvo com sucesso!')
        except ValueError as err:
            return HttpResponse(f'Erro: {err}')