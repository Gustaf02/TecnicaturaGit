/*
 Ejercicio 2: Leer 5 números. Guardarlos en un arreglo y mostrarlos en orden inverso al introducido
 */
package arreglos_ejercicio_2;

import java.util.Scanner;


public class Arreglos_Ejercicio_2 {

   
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        
         float numeros[]  = new float [5];
        System.out.println("Guardando los datos del arreglo");
        
        for (int i= 0; i<5 ; i++){
            System.out.println((i+1)+ "Digite un número ");
        numeros [i]= entrada.nextFloat();
        }
        
            System.out.println("\nImprimir los elementos del arreglo");
            for (int i= 4; i>=0 ; i--){
                System.out.print(i + " " + numeros[i]);
                
            }
            System.out.println("\n");
    }
    
}
