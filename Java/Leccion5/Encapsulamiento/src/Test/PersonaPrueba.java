/*
 
 */
package Test;

import dominio.Persona;  // se puede usar * para importar todas las clases 

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona ("Osvaldo",57000, false);
        System.out.println("persona1, su nombre es: "+ persona1.getNombre());
        
        //modificar a través de los métodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre="Juan Ignacio"; ya no se puede utlizar
        //System.out.println("Nombre es: "+ persona1.nombre)   Error
        System.out.println("persona1, con su nombre modificado: "+ persona1.getNombre());
        System.out.println("persona1, su sueldo es: "+ persona1.getSueldo());
        System.out.println("persona1, para obtener el booleano: "+ persona1.isEliminado());
        
     // Tarea: crear otro objeto de tipo persona, asignar valores de manera inicial, e imprimir, 
     // modificar sus valores y volver a imprimir 
        Persona persona2 = new Persona ("Roco",60000, false);
        System.out.println("persona2, su nombre es: "+ persona2.getNombre());
        
        //modificar a través de los métodos
        persona2.setNombre("Diego");
        
        System.out.println("persona2, con su nombre modificado: "+ persona2.getNombre());
        System.out.println("persona2, su sueldo es: "+ persona2.getSueldo());
        System.out.println("persona2, para obtener el booleano: "+ persona2.isEliminado());
        
        //System.out.println("persona1" + persona1.toString()); Es lo mismo lo de abajo. No es nec. poner toString
        System.out.println("persona1" + persona1);
        
        }
}
