var nombre = 'José';
var apellido = 'Montés';
var nombreCompleto = nombre + apellido;
console.log(nombre);
var nombreCompleto2 = 'Ariel' + ' '+ 'Betancud';
console.log(nombreCompleto);
var juntos = nombre + 219;
console.log(juntos);
juntos =  nombre + 17 + 18;  // Lee de izquierda a derecha
console.log(juntos)
juntos = 17 + 18 + nombre;
console.log(juntos);
nombre += apellido;
console.log(nombre);

//hoy ya no se usa var, se usa let y const
let nombre2 = "Pedro";
console.log(nombre2);
const apellido2 = "Gómez";
console.log(apellido2)

let x, y; // se pueden crear varias variables dentro de una misma línea
x= 17, y =21;  // se puede hacer asignación de variables dentro de la misma línea
let z = x + y; // se asigna el valor de la operación
console.log(z);

let _1num = 31;  // no utilizar números para iniciar el valor de una variable
let rompiendo = "rompe" // no utilizar palabras reservadas para variables

console.log(_1num)
console.log(rompiendo)

