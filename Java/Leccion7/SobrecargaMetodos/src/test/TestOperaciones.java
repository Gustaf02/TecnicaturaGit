/*

 */
package test;

import operaciones.Operaciones;


public class TestOperaciones {
    public static void main(String[] args) {
        var resultado = Operaciones.sumar(7,9);
        System.out.println("resultado " + resultado);
        
        var resultado2 = Operaciones.sumar(5.0, 7);
        System.out.println("resultado 2  " + resultado2);
        
        var resultado3 = Operaciones.sumar(8, 6L);  // 6 Long
        System.out.println("resultado 3 " + resultado3);
    }
    
    
}
