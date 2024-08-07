var valor1 = document.getElementById("cantidad");
    var valor2 = document.getElementById("cant_strick");
    var valor3 = document.getElementById("cant_bolas");
    var valor4 = document.getElementById("cant_recta");
    var valor5 = document.getElementById("rectas");
    var valor6 = document.getElementById("curvas");
    var valor7 = document.getElementById("cambio");
    var fecha = document.getElementById("fecha");
    var resultado1 = document.getElementById("porcentaje_strick");
    var resultado2 = document.getElementById("porcentaje_bolas");

    valor4.addEventListener("input", calculapromedio);

    function calculapromedio(){
        valor1 = parseFloat(valor1.value);
        valor2 = parseFloat(valor2.value);
        valor3 = parseFloat(valor3.value);
        var promedio = (valor2/valor1)*100;
        resultado1.value = promedio;
        var promedio2 = (valor3/valor1)*100;
        resultado2.value = promedio2;
        console.log('validacion');
    };

    function validar2(){
          var recta = parseFloat(valor5.value);
          var  curva = parseFloat(valor6.value);
          var  cambio = parseFloat(valor7.value);
          var suma = valor2 + valor3;
          var suma2 = recta  + curva + cambio
         console.log("validacion de valor completo ");
         console.log(suma2)

        if (valor1.value===""||valor2.value===""||valor4.value===""||fecha.value===""){
           
            Swal.fire({
                      title: 'CAMPOS VACIOS!',
                      text: 'Porfavor complete todo los  Campos',
                      icon: 'warning',
                    });
            return false;
        }if (valor1 != suma){
            Swal.fire({
                      title: '!!ERROR VALORES INVALIDO!!',
                      text: 'La Cantidad de lanzamiento ingresado no conside con los datos ingresado',
                      icon: 'error',
                     });
            return false;
        }if (valor1 != suma2) {
            Swal.fire({
                      title: '!!ERROR VALORES INVALIDO: TIPOS DE LANZAMIENTO!!',
                      text: 'La Cantidad de lanzamiento ingresado no conside con los datos ingresado',
                      icon: 'error',
                     });;
            return false;
        }
        Swal.fire({
        position: 'center',
        icon: 'success',
        title: 'Se  ah guardado Correctamente  los datos del Entrenamiento',
        showConfirmButton: false,
        timer: 1550000
        });
       return  true;

      
    }


