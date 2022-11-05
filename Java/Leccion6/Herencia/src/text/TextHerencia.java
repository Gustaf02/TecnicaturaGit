/*
 
 */
package text;

import domain.Cliente;
import domain.Empleado;
import domain.Persona;
import java.util.Date;


public class TextHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Ariel",57000.0 );
        
        System.out.println("Empleado 1 = " + empleado1);
    /*    
        Date fecha = new Date();
        
        Cliente cliente1 = new Cliente(new Date(), true, "Bety", 'F', 32, "9 de julio 1413");
        System.out.println("cliente "+ cliente1);
        
        Persona persona1 = new Persona();
    } */
}
}