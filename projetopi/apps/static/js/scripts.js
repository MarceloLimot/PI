function sair(){
    window.location = "/"
}

function teste(){
    alert("entrou no javascript")
}

function sairAdmin() {
    window.history.back()
}

function sairADM(){
    window.location.replace("adminarea")
}


//----------Funções de Cadastro----------\\
function cadDonat(){
    window.location = "cadDonat"
}

function cadDoador(){
    window.location = "cadDoador"
}

function cadFunc(){
    window.location = "cadFunc"
}



//----------Funções de Edição----------\\ 
function editFunc(){
    window.location = "editFunc"
}

function editDonat(){
    window.location = "editDonat"
}

function editDoador(){
    window.location = "editDoador"
}



//----------Funções de Edição----------\\ 
function deleteFunc(){
    window.location = "deleteFunc"
}

function deleteDonat(){
    window.location = "deleteDonat"
}

function deleteDoador(){
    window.location = "deleteDoador"
}


//----------Funções para listar Logins----------\\
function listaLogin(){
    window.location = "listaLogin"
}

function listaDonat(){
    window.location = "listaDonat"
}

function listaDoador(){
    window.location = "listaDoador"
}


//--------------------Evento para mostrar/esconder senha--------------------\\
document.getElementById('olho').addEventListener('mousedown', function() {
    document.getElementById('senha').type = 'text';
  });
  
  document.getElementById('olho').addEventListener('mouseup', function() {
    document.getElementById('senha').type = 'password';
  });
  
  // Para que o password não fique exposto apos mover a imagem.
  document.getElementById('olho').addEventListener('mousemove', function() {
    document.getElementById('senha').type = 'password';
  });
//------------------Fim do Evento para mostrar/esconder senha------------------\\

function areaAdmin(){
    const senha = document.querySelector("#senha");
    const nome = document.querySelector("#nome");
    const vNome = nome.value;
    const vSenha = senha.value;
    if(vNome=="" || vSenha==""){
        alert("um dos campos esta vazio!")
    }
    else{
        if(vNome=="admin" & vSenha=="1234"){
            window.location.replace("adminarea")
        }
        else{
            window.location.replace("areadoador")
        }
    }
}