/*
 
 */
package Operaciones;


public class Aritmetica {
    // Atributos de clase
    int a;
    int b;
    
    // El constructor es un método especial. Construye un objeto, reserva un espacio
    // de memoria e inicilializa los atributos de la clase
    
    public Aritmetica(){ // no es necesario colocarlo    Constructor 1
        System.out.println("Se está ejecutando el constructor número 1");
    }
    
    public Aritmetica(int a, int b){  // Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se está ejecutando el constructor número 2");
    }
    
    // Método 
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("El resultado es " + resultado);
    }
     
    // Otro método
    public int sumarConRetorno(){
       // int resultado = a + b;
        return a + b;
       // también se puede colocar return this.a + this.b; 
    
}
    // Un método más
      // modificador de acceso + tipo de retorno + identificador 
    public int sumarConArgumentos(int arg1, int arg2){
        this.a = arg1;  // podemos usar this o no. El arguento a se asigna al atributo this.a 
        this.b = arg2;  // el this hace que sea más legible. 
     //   return a + b; 
        return sumarConRetorno();
}
}