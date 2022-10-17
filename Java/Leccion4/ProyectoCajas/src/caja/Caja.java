/*
 *
 */
package caja;


public class Caja {  //Caja pública caja
    // Atributos, características
    int ancho;
    int alto;
    int profundo;
    
    // métodos y constructores (acciones)
    public Caja(){} // Constructor vacío 
    
    // Constructor con parámetros
    public Caja(int ancho, int alto, int profundo) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen(){ //método para calcular
        return alto * ancho * profundo;
    } 
    
    
    
}
