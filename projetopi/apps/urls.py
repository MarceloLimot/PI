from django.urls import path
from . import views

urlpatterns = [

#----------------/Path para paginas publicas\----------------#   
    path('', views.index, name='index'),
#    path('login',views.login, name='login'),
    path('sobre',views.sobre, name='sobre'),
    path('contato',views.contato, name='contato'),
    path('adminarea', views.adminarea, name='adminarea'),
    path('areadoador', views.areadoador, name='areadoador'),
#-------------/Fim do path para paginas publicas\-------------#  


#------------------/path para listar Logins\------------------#
    path('listaLogin', views.listaLogin, name='listaLogin'),
    path('listaDonat', views.listaDonat, name='listaDonat'),
    path('listaDoador', views.listaDoador, name='listaDoador'),
#---------------/Fim do path para listar Logins\---------------#


#----------------/path para cadastro de Logins\----------------#
    path('cadFunc', views.cadFunc, name='cadFunc'),
    path('cadDonat', views.cadDonat, name='cadDonat'),
    path('cadDoador', views.cadDoador, name='cadDoador'),
#-------------/Fim do path para cadastro de Login\-------------#


#-----------------/path para update de Logins\-----------------#
    path('editFunc/<int:id>',views.editFunc, name='editFunc'),  
    path('editDonat/<int:id>',views.editDonat, name='editDonat'),
    path('editDoador/<int:id>',views.editDoador, name='editDoador'),
#--------------/Fim do path para update de Login\--------------#


#-----------------/path para delete de Logins\-----------------#
    path('deleteFunc/<int:id>',views.deleteFunc, name='deleteFunc'),  
    path('deleteDonat/<int:id>',views.deleteDonat, name='deleteDonat'),
    path('deleteDoador/<int:id>',views.deleteDoador, name='deleteDoador'),
#--------------/Fim do path para delete de Logins\--------------#

   
]