/*
 
 */
package Operaciones;


public class Aritmetica {
    // Atributos de clase
    int a;
    int b;
    
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