from django import forms

from .models import LoginFunc, LoginDonat, LoginDoador


#-----------------Form para cadastro de Funcionario-----------------#
class cadFuncForm(forms.ModelForm):

    class Meta:
        model = LoginFunc
        fields = ('nome','telefone','email','senha')
#-----------------Fim do Form para cadastro de Funcionario-----------------#


#-----------------Form para cadastro de Donatarios-----------------#
class cadDonatForm(forms.ModelForm):

    class Meta:
        model = LoginDonat
        fields = ('nome','telefone','email','senha', 'rua', 'numero', 'bairro', 
        'cep', 'complemento', 'cidade', 'estado')
#-----------------Fim do Form para cadastro de Donatarios-----------------#


#-----------------Form para cadastro de Doadores-----------------#
class cadDoadorForm(forms.ModelForm):

    class Meta:
        model = LoginDoador
        fields = ('nome','telefone','email','senha', 'rua', 'numero', 'bairro', 
        'cep', 'complemento', 'cidade', 'estado')
#-----------------Fim do Form para cadastro de Doadores-----------------#