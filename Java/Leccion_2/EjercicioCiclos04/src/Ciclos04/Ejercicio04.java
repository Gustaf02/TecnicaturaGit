/*
 * Ejecicio 04: Pedir números hasta que se tecle uno negativo, y mostrar cuántos 
elementos se han introducido. Lo hacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane
 */
package Ciclos04;

import javax.swing.JOptionPane;


public class Ejercicio04 {
    public static void main(String[] args) {
        
        int numero, conteo =0;
        
       numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número ")); 
        
        while (numero >= 0){
            JOptionPane.showMessageDialog(null,"El número "+ numero +" es positivo");
            conteo ++;
             numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
           
        }
        JOptionPane.showMessageDialog(null,"Ha ingresado "+ conteo +" que no son negativos");
    } 
        
        
    }

