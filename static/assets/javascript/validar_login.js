
var btnEnviar = document.getElementById('boton');
var caja2 = document.getElementById('clave');
var caja1 = document.getElementByIdç('username')

btnEnviar.disabled = true;
caja2.disabled = true;

function verificar2(valor){
    if (caja2.value.length>=5){
      btnEnviar.disabled = false;
      btnEnviar.classList.remove("disabled");
    }else{
      btnEnviar.disabled = true;
    }
  }

function verificar1(valor){
    if (valor.length>=5){
      caja2.disabled = false;
    }else{
      caja2.disabled = true;
      caja2.value = "";
      btnEnviar,disabled = true;;

    }
  }