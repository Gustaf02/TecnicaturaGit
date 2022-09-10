/*
 Ejercicio 3: leer los números hasta que se introduzca un 0;
Para cada uno indicar si es par o impar
Primero lo haremos con la frase Scanner, Luego con la clase OptionPane
 */
package Ciclos03;

import java.util.Scanner;


public class Ciclos03 {
    public static void main(String[] args) {
           
    Scanner entrada = new Scanner (System.in);
    
    int numero;
    
        System.out.println("Digite un número");
        numero = Integer.parseInt(entrada.nextLine());
        
    while (numero !=0){
        if (numero % 2 == 0) {
            System.out.println("El número ingresado es par");
        }
        else{
            System.out.println("El número ingresado es impar");
        }
        System.out.println("Digite otro número");
        numero = Integer.parseInt(entrada.nextLine());
    }
        System.out.println("El número ingresado es: " + numero);    
    }
}
   
