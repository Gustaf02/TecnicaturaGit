/*
 Ejercicio 3: Leer 5 números por teclado, almacenarlos en un arreglo, y a continuación realizar
la media de los números positivos, la media de los números negativos, y contar el número de 0
 */
package arreglos_ejercicio_3;

import java.util.Scanner;


public class Arreglos_Ejercicio_3 {

    
    public static void main(String[] args) {
          Scanner entrada = new Scanner (System.in);
        
         float numeros[]  = new float [5];
         float negativos= 0, positivos = 0, mediaNegativos, mediaPositivos;
         int conteoO = 0, conteo_negativo = 0, conteo_positivo = 0;
         
         System.out.println("Guardando los datos del arreglo");
        
        for (int i= 0; i<5 ; i++){
            System.out.println((i+1)+ "Digite un número ");
        numeros [i]= entrada.nextFloat();
        
        if (numeros [i]>0){
            positivos += numeros[i];
            conteo_positivo ++;
        }
        
            else if (numeros [i]<0){
                    negativos += numeros[i];
                    conteo_negativo ++;
                    }
            else {
                conteoO++;
                
        }
        if (conteo_positivo == 0){
            System.out.println("No se puede sacar la media de los números +");}
        else {
            mediaPositivos = positivos / conteo_positivo;
            System.out.println("La media de los números positivos es" + mediaPositivos);
        }
         if (conteo_negativo == 0){
            System.out.println("No se puede sacar la media");}
        else {
            mediaNegativos = negativos / conteo_negativo;
            System.out.println("La media de los números negativos es " + mediaNegativos);
             
                        
        }
            System.out.println("La cantidad de 0 es " + conteoO);         
    }
    
    }}
