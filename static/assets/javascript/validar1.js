    var valor1 = document.getElementById("turno");
    var valor2 = document.getElementById("hits");
    var valor4 = document.getElementById("ponche");
    var resultado1 = document.getElementById("Average");
    var fecha = document.getElementById("fecha");
    var ponche = document.getElementById("ponche");



    valor4.addEventListener("input", calculapromedio);

    function calculapromedio(){
        valor1 = parseFloat(valor1.value);
        valor2 = parseFloat(valor2.value);

        var promedio = valor2/valor1;
        resultado1.value = promedio;
         console.log(valor1)
        console.log(valor2)

    };

     function validar(){
 
      console.log('validaion de campos')
       console.log(valor1)
        console.log(valor2)


        if (valor1.value==""||valor2.value===""||valor4.value===""||fecha.value===""||ponche.value===""){
            Swal.fire({
                      title: 'CAMPOS VACIOS!',
                      text: 'Porfavor complete todo los  Campos',
                      icon: 'warning',
          
             });
            return false;
        }if (valor2 > valor1){
          Swal.fire({
                      title: '!!ERROR VALORES INVALIDO!!',
                      text: 'El  valor ingresado en el campo hits es mayor que los turnos',
                      icon: 'error',
          
             });

          return false;
        }
       
     
        Swal.fire({
        position: 'center',
        icon: 'success',
        title: 'Se  ah guardado Correctamente  los datos',
        showConfirmButton: false,
        timer: 1550000
        });

       return true; 
    }