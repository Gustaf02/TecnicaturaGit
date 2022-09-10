/*
Ejercicio 3: leer los números hasta que se introduzca un 0;
Para cada uno indicar si es par o impar
Primero lo haremos con la frase Scanner, Luego con la clase OptionPane
 */
package Ciclos03;

import javax.swing.JOptionPane;




public class Ejercicio03 {
    public static void main(String[] args) {
        
            
    int numero;
    
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        
    while (numero !=0){
        if (numero % 2 == 0) {
           JOptionPane.showMessageDialog(null,"El número ingresado es "+numero+" par");
        }
        else{
             JOptionPane.showMessageDialog(null,"El número ingresado es "+numero+" impar");
        }
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
    }
        JOptionPane.showMessageDialog(null,"El número ingresado es " +numero+ ". Finaliza el programa");    
    }
        
        
    }

