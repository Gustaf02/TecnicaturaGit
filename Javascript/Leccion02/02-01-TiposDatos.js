// Tipos de datos en JavasScript
var nombre = 'Ariel'; //Tipo String
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 3.4;
console.log(typeof nombre);

// Tipo numérico
var numero = 3000;
console.log(numero);

// Tipo objeto
var objeto = {
    nombre: 'Ariel',
    apellido: 'Betancud',
    telefono: '2343672'
}
console.log(objeto);

// Tipo de datos booleanos
var bandera = true;
console.log(bandera);

// Tipo de dato función (permite reutilizar líneas de código)
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo de dato symbol
var simbolo = Symbol('Mi símbolo')
console.log(simbolo);

// Tipo de clase 
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona);