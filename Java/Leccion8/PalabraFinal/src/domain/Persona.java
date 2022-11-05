/*
 
 */
package domain;

public class Persona {           // es una clase constante
    
    public final static int CONSTANTE_AQUI = 15;  // atributo constante. Se combina con static. Se coloca en mayúscula
    private String nombre;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public  void imprimir (){
        System.out.println("Es un método para imprimir");
        
        
}
}
