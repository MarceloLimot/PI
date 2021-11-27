from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user, get_user_model

class App(models.Model):

    STATUS = (
        ('em processo...','Em processo...'),
        ('finalizado','Finalizado')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=25,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class LoginFunc(models.Model):
    permissoes=(
        ('admin','Admin'),
        ('user','User')
    )
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=16,null=True, blank=True)
    email = models.CharField(max_length=100,null=True, blank=True)
    senha  = models.CharField(max_length=255)
    nivel = models.CharField(
        max_length=25,
        choices=permissoes,
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class LoginDonat(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=16,null=True, blank=True)
    email = models.CharField(max_length=100,null=True, blank=True)
    senha = models.CharField(max_length=15)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    complemento  = models.CharField(max_length=100,null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class LoginDoador(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=16,null=True, blank=True)
    email = models.CharField(max_length=100,null=True, blank=True)
    senha = models.CharField(max_length=15)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    complemento  = models.CharField(max_length=100,null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome




#class Doacao(models.Model):
#    status=(
#        ('doado','Doado'),
#        ('comprovado', 'Comprovado')
 #   )
#    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#    valor= models.CharField(max_length=25)
#    valorStatus=models.CharField(
#        max_length=25,
#        choices=status,
#    )

#    status2=valorStatus.value_to_string
#    title= 'Doação Status: '
#    criado_em = models.DateTimeField(auto_now_add=True)
#    atualizado_em = models.DateTimeField(auto_now=True)

#class Identifie(user1,senha1):
 #   def login1(self, user1, senha1):
#        vNome = user1
#        vSenha = senha1
#        if(vNome=="" or vSenha==""):
#            alert("um dos campos esta vazio!")
#        
#        else:
#            alert("nome: "+ vNome +" Senha: "+ vSenha)
#            if(vNome=="admin" and vSenha=="1234"):
#                alert("Senha correta")
#                window.location.replace("sobre.html")
#            else:
#                alert("Usuario ou Senha incorretos")
        
    