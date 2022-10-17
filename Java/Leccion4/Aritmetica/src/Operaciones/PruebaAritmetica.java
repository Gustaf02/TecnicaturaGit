/*
 
 */
package Operaciones;


public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10;  // puede ir var o int pero var no se pueden poner en atributos o parámetros
        int b = 7;  // variables locales
                    // memoria stack
        miMetodo(); //llamamos al método nuevo
        
        Aritmetica aritmetica1 = new Aritmetica(); // Se creó el objeto aritmetica1
        
        aritmetica1.a = 3; 
        aritmetica1.b = 7;
        
        aritmetica1.sumarNumeros();
        // para almacenar un objeto o los atributos se utiliza la memoria heap
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado "+ resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos" + resultado);
        
        System.out.println("aritmética a" + aritmetica1.a);
        System.out.println("aritmética b" + aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5,8);
        System.out.println("aritmética 2" + aritmetica1.a);
        System.out.println("aritmética 2" + aritmetica1.b);
        
        Persona persona = new Persona("Ariel", "Betancud");
        System.out.println("persona" + persona);
        System.out.println("Persona nombre " + persona.nombre);
        System.out.println("Persona nombre " + persona.apellido);
        
    // Modularidad: creamos un nuevo método
        }
    public static void miMetodo(){
          // a = 10; una variable está limitada
            System.out.println("Acá hay otro método");  
    }
}
// Creamos una nueva clase, pero ya no será publica 
class Persona {
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ //constructor
        
        super();  // Llamada el constructor de la clase Padre object
    //    Imprimir imprimir = new Imprimir();
     new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto Persona usando this " + this);
    }
    
}
class Imprimir{ 
public Imprimir (){
    super(); // El constructor de la clase Padre para reservar memoria
} 
   public void imprimir (Persona persona){
     System.out.println("Persona desde la clase imprimir " + persona);
    System.out.println("Impresión del objeto actual (this) " + this);
}
}