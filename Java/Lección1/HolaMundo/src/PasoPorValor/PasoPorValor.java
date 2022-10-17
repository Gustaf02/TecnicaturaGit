/*
 
 */
package PasoPorValor;

public class PasoPorValor {
    public static void main(String[] args) {
        var valorX = 20; 
        System.out.println("valor x "+ valorX);
        cambioValor(valorX); // Sólo le enviamos una copia
        System.out.println("valor x " +  valorX);
    }
    public static void cambioValor(int arg1){ //parámetro por valor
        System.out.println("arg1= "+ arg1);
        arg1 = 15; 
    }
}
