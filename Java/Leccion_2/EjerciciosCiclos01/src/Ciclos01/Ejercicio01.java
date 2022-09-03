/*
Ejercicio 1: Leer un número y leer su cuadrado. Repetir el proceso hasta que se introduzca un número negativo
sin clase Scanner*/
package Ciclos01;

import javax.swing.JOptionPane;


public class Ejercicio01 {
    public static void main(String[] args) {
        
        int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número" )); //toma String por eso Integer
        while (numero>=0){  // Número mayor a 0 o positivo
            cuadrado = (int)Math.pow(numero,2);
            System.out.println("El número "+ numero + "elevado al cuadrado es " + cuadrado );
            
            System.out.println("Digite otro número ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número número" ));
        }
        
        System.out.println("El programa ha finalizado por número negativo");
       
               
    }
        
    }

