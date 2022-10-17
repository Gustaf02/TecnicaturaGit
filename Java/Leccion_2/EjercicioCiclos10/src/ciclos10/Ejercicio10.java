/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ciclos10;

import javax.swing.JOptionPane;


public class Ejercicio10 {
    public static void main(String[] args) {
          int numero, suma= 0;
        
        for(int i=1; i <= 10; i++){
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
            suma += numero;
        }
       JOptionPane.showMessageDialog(null,"La suma de todos los números es " +suma);
                
    }
        
               
    }
      
        
       
    
    
    
