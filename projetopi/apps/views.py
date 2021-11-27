from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, request
from apps.models import App, LoginFunc, LoginDonat, LoginDoador
#from .models import Login
from .forms import cadFuncForm, cadDonatForm, cadDoadorForm
import datetime
from django.contrib import messages



########################################################################
                            #cadastro#
########################################################################
#----------------/funcao para cadastro de funcionario\----------------#
@login_required
def cadFunc(request): 
    if request.method == 'POST':
        form= cadFuncForm(request.POST)
        if form.is_valid():
            LoginFunc = form.save(commit=False)
            LoginFunc.nivel = 'user'
            LoginFunc.save()
            return redirect('/adminarea')
    else:
        form = cadFuncForm()
        return render(request,'apps/cadfunc.html',{'form': form})
#-------------/Fim da funcao de cadastro de funcionarios\-------------#


#-----------------/funcao para cadastro de donatario\-----------------#
def cadDonat(request):
    if request.method == 'POST':
        form= cadDonatForm(request.POST)
        if form.is_valid():
            LoginDonat = form.save(commit=False)
            LoginDonat.save()
            return redirect('/adminarea')
    else:
        form = cadDonatForm()
        return render(request,'apps/caddonat.html',{'form': form})
#--------------/Fim da funcao de cadastro de donatario\--------------#


#------------------/funcao para cadastro de doador\------------------#
def cadDoador(request):
    if request.method == 'POST':
        form = cadDoadorForm(request.POST)
        if form.is_valid():
            LoginDoador = form.save(commit=False)
            LoginDoador.save()
            return redirect('/adminarea')
    else:
        form = cadDoadorForm()
        return render(request, 'apps/caddoador.html',{'form': form})
#---------------/Fim da funcao de cadastro de doador\---------------#



########################################################################
                            #Updates#
########################################################################
#----------------/funcao para update de funcionario\----------------#
@login_required
def editFunc(request, id): 
    func = get_object_or_404(LoginFunc, pk=id)
    form = cadFuncForm(instance=func)

    if request.method == 'POST':
        form = cadFuncForm(request.POST, instance=func)

        if(form.is_valid()):
            func.save()
            return redirect('/adminarea')  
        else:
            return render(request,'apps/editfunc.html',{'form': form, 'task':func})                  
    else:
        return render(request,'apps/editfunc.html',{'form': form, 'task':func})
#-------------/Fim da funcao para update de funcionario\-------------#


#------------------/funcao para update de Donatario\------------------#
@login_required
def editDonat(request, id):
    donat = get_object_or_404(LoginDonat, pk=id)
    form = cadDonatForm(instance=donat)

    if(request.method == 'POST'):
        form = cadDonatForm(request.POST, instance=donat)

        if(form.is_valid()):
            donat.save()
            return redirect('/adminarea')
        else:
            return render(request, 'apps/editdonat.html',{'form': form, 'task':donat})    
    else:
        return render(request, 'apps/editdonat.html',{'form': form, 'task':donat})
#---------------/Fim da funcao para update de Donatario\---------------#


#------------------/funcao para update de Doador\------------------#
@login_required
def editDoador(request, id):
    doador = get_object_or_404(LoginDoador, pk=id)
    form = cadDoadorForm(instance=doador)

    if(request.method == 'POST'):
        form = cadDoadorForm(request.POST, instance=doador)

        if(form.is_valid()):
            doador.save()
            return redirect('/adminarea')
        else:
            return render(request, 'apps/editdoador.html',{'form': form, 'task':doador})    
    else:
        return render(request, 'apps/editdoador.html',{'form': form, 'task':doador})
#---------------/Fim da funcao para update de Doador\---------------#



########################################################################
                            #Deletar Logins#
########################################################################
#------------------/funcao para delete de Funcionario\------------------#
@login_required
def deleteFunc(request, id):
    func = get_object_or_404(LoginFunc, pk=id)
    func.delete()
    return redirect('/listaLogin') 
#---------------/Fim da funcao para delete de Funcionario\---------------#


#------------------/funcao para delete de Donatario\------------------#
@login_required
def deleteDonat(request, id):
    donat = get_object_or_404(LoginDonat, pk=id)
    donat.delete()
    return redirect('/listaDonat') 
#---------------/Fim da funcao para delete de Donatario\---------------#

#------------------/funcao para delete de Doador\------------------#
@login_required
def deleteDoador(request, id):
    doador = get_object_or_404(LoginDoador, pk=id)
    doador.delete()
#    messages.info(request, "Doador Deletado com Sucesso.")
    return redirect('/listaDoador')
#---------------/Fim da funcao para delete de Doador\---------------#



########################################################################
                            #Listar Logins#
########################################################################
#----------------/Retorna os Funcionarios cadastrados\----------------#
@login_required
def listaLogin(request):
    listLogin = LoginFunc.objects.all().order_by('-criado_em')
    paginator = Paginator(listLogin, 2)
    page = request.GET.get('page')
    Login = paginator.get_page(page)

    return render(request,'apps/listaLogin.html', {'logins':Login})
#--------------------------/ Fim do retorno\--------------------------#

#-----------------/Retorna os Donatarios cadastrados\-----------------#
@login_required
def listaDonat(request):
    listLogin = LoginDonat.objects.all().order_by('-criado_em')
    paginator = Paginator(listLogin, 2)
    page = request.GET.get('page')
    Login = paginator.get_page(page)
    return render(request, 'apps/listaDonat.html', {'logins':Login})
#--------------------------/ Fim do retorno\--------------------------#

#------------------/Retorna os Doadores cadastrados\------------------#
@login_required
def listaDoador(request):
    listLogin = LoginDoador.objects.all().order_by('-criado_em')
    paginator = Paginator(listLogin, 2)
    page = request.GET.get('page')
    Login = paginator.get_page(page)
    return render(request, 'apps/listaDoador.html', {'logins':Login})
#--------------------------/ Fim do retorno\--------------------------#



########################################################################
                            #OUTROS#
########################################################################

def inicio(request):
    return HttpResponse('inicio')

def index(request):
    return render(request,'apps/index.html')

def login(request):
    return render(request,'login.html')

def sobre(request):
    return render(request,'apps/sobre.html')

def contato(request):
    return render(request,'apps/contato.html')



########################################################################
#-------------------Busca o cadastro solicitado------------------------#
########################################################################
#-------------/Retorna lista de Funcionarios cadastrados\--------------#
@login_required
def usuarioLista(request, id):
    userlist = get_object_or_404(App, pk=id)
    paginator = Paginator(userlist, 5)
    page = request.GET.get('page')
    user = paginator.get_page(page)
    return render(request, 'apps/usuario.html', {'task':user})

@login_required
def usuarioView(request, id):
    user = get_object_or_404(LoginFunc, pk=id)
    return render(request, 'apps/dadosDonatario.html', {'task':user})

@login_required
def dadosDonatario(request, id):
    user = get_object_or_404(LoginFunc, pk=id)
    return render(request, 'apps/dadosDonatario.html', {'task':user})



########################################################################
                            #OUTROS#
########################################################################
@login_required
def adminarea(request):
    return render(request,'apps/adminarea.html')

def areadoador(request):
    return render(request,'apps/areadoador.html')



########################################################################
                            #Login#
########################################################################
def verTipoLogin(request, id):  
    func = get_object_or_404(LoginFunc, pk=id)
    func = get_object_or_404(LoginDonat, pk=id)
    func = get_object_or_404(LoginDoador, pk=id)