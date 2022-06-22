
package Leccion2;


public class Leccion2 {
    
    public static void main(String[] args) {
        var condicion = false;
        if (condicion){
            System.out.println("Condición verdadera");//condicional simple
        }
        else {
            System.out.print("Condición falsa");//condicional doble
        }
                             
        var numero = 2;
        var numTexto = "número desconocido";
        if (numero ==1){
            numTexto = "Número uno";
        } 
        else if (numero ==2){
            numTexto = "Número 2";
        }
         else if (numero ==3){
            numTexto = "Número 3";
        }
         else if (numero ==4){
            numTexto = "Número 2";
        }
         else {
            numTexto = "Número no encontrado";
        }
        System.out.println("número texto"+ numTexto);
        }                
}
