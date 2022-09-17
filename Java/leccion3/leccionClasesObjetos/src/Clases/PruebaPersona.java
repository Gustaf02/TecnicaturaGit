/*
 
 */
package Clases;


public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); // Se llama al constructor (permite asignar valores al objeto)
        persona1.nombre = "Gustavo";  // El valor hexadecimal comienza con 0x
        persona1.apellido = "Ortiz";
        
        persona1.obtenerInformacion();
        
        // Creamos un objeto 2
        Persona persona2 = new Persona();
        System.out.println("Persona 2 "+ persona2);
        System.out.println("Persona 2 "+ persona1);
        // si ejecutamos paquete clase, clase persona y dirección de memoria
        persona2.obtenerInformacion();
        
        persona2.nombre = "Ariel";
        persona2.apellido = "Betancud";
        persona2.obtenerInformacion();
    }
    
}
