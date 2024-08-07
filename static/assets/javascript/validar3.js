function validar(){
        var peso = document.getElementById("edad");
        var altura = document.getElementById("altura");
        pesoNum = parseFloat(peso.value);
        console.log(pesoNum);

        if (isNaN(pesoNum)||pesoNum<=5 ||pesoNum>=200){
             Swal.fire({
                    title: '!!ERROR PESO!!',
                    text: 'Porfavor  Ingrese un valor valido en el Campo',
                    icon: 'error',
          
                    });
            return false;
        }
        alturaNum = parseFloat(altura.value);
        if (isNaN(alturaNum)||alturaNum<=0.50||altura>=2.50 ){
            Swal.fire({
                    title: '!!ERROR ALTURA!!',
                    text: 'Porfavor  Ingrese un valor valido en el Campo',
                    icon: 'error',
          
                    });
            return false;
        }
        Swal.fire({
        position: 'center',
        icon: 'success',
        title: 'Se  ah guardodo Correctamente  los datos',
        showConfirmButton: false,
        timer: 1550000
        });
        return true;
    }