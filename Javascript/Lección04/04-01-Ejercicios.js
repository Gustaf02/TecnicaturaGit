// Ejercicio 1: Calcular estación del año
let mes = 9;
let estacion;
if (mes==1||mes==2||mes==12){
    estacion="verano";
}
else if (mes==3||mes==4||mes==5){
    estacion="otoño";
}
else if (mes==6||mes==7||mes==8){
    estacion="invierno";
}
else if (mes==9||mes==10||mes==11){
    estacion="primavera";
}
else{
    estacion="Valor incorrecto"
}
console.log("El mes corresponde al mes de "+ estacion);


// Ejercicio 2: Hora del día
let horaDia = 21;
let mensaje;
if (horaDia >= 6 && horaDia <=11){
    mensaje ="Buenos días"
}
else if (horaDia >= 12&& horaDia <=16){
    mensaje="Buenas tardes";
}
else if (horaDia >= 17&& horaDia <=19){
    mensaje="Hola, buenas tardes";
}
else if (horaDia >= 20&& horaDia <=23){
    mensaje="Buenas noches";
}
console.log("El saludo correspondiente es " + mensaje)

// Estructura switch  se pueden utilizar números y cadenas. Sintaxis igual a java
switch (mes){
    case 1: case 2: case 12:
        estacion ="verano";
        break
    case 3: case 4: case 5:
        estacion ="otoño";
        break
    case 6: case 7: case 8:
        estacion ="invierno";
        break
    case 9: case 10: case 11:
        estacion ="primavera";
        break
    default:
        estacion = "valor incorrecto";
console.log("la estación es  "+ estacion);
}


