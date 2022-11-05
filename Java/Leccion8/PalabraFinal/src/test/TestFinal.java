/*
Uso de la palabra final. Tiene diferentes significados dependiendo de donde se aplique
variables: evita cambiar el valor que almacena la variable
métodos: evita que se modifique la definición o el comportamiento de un método desde una subclase (hija)
clase: evita que se creen clases hijas
Otra característica es que normalmente, cuando trabajamos con variables, se combina con el modificador de acceso
estático para convertir una variable en una constante, es decir que no se puede modificar su valor. 
El ejemplo de esto es la clase Math en la cual todos sus atributos son de tipo estático y final, es por esto que 
pi se conoce como una constante. 

 */
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 34556987;
        System.out.println("Dni " + miDni);
        
       // miDni = 3245678; no se puede modificar
       //miDni = 34568  No se puede modificar
        //Persona.CONSTANTE_AQUI = 9            No se modifica
        System.out.println("Mi atributo constante es " + Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona(); // ya existe un constructor vacío
        //persona1 = new Persona(); no se puede agregar una nueva referencia 
        
        persona1.setNombre("Ariel Bentancud");
        System.out.println("persona 1: " + persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("persona 1: " + persona1.getNombre());
        
               
    }
}
