/*
Ejercicio 1: crear un proyecto según las especificaciones mostradas a continuación
la fórmula es volumen * ancho * alto * profundidad
 */
package caja;


public class PruebaCaja {
    public static void main(String[] args) { // método main
        // Variables locales
        int medidaAncho = 3;  //valores ingresados en código duro
        int medidaAlto = 2; 
        int medidaProf = 6; 
        
        Caja caja1 = new Caja();//instanciamos el objeto, constructor vacío
        caja1.ancho = medidaAncho;
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        
        int resultado = caja1.calcularVolumen();  //llamamos al método
        // Primer resultado
        System.out.println("resultado de volumen de caja 1: "+ resultado);
        
         Caja caja2 = new Caja(2,4,6); //llamamos al constructor 2 con nuevos argumentos
        // llamamos con el nuevo objeto al método para un nuevo cálculo
        System.out.println("Resultado volumen de caja 2: "+ caja2.calcularVolumen());
         
        
        
        
        
        
        
    }
}
