
package Ejercicio3;

import java.util.Scanner;

public class Ejercicio3 {
    
Scanner entrada=new Scanner(System.in);

public static void main(String[] args) {
    
    Scanner entrada= new Scanner(System.in);
        System.out.println("¿Cuál es la base del rectángulo: ");
    int baseRectangulo = Integer.parseInt(entrada.nextLine());
        System.out.println("¿Cuál es la altura del rectángulo: ");
       
int alturaRectangulo = Integer.parseInt(entrada.nextLine());

int area = baseRectangulo * alturaRectangulo;

int perimetro = baseRectangulo * alturaRectangulo;
        System.out.println("Área del rectángulo:");

System.out.println("Perímetro del rectángulo: ");
System.out.println("¿Cuál es la altura del rectángulo: ");

var operadorT = (baseRectangulo > alturaRectangulo) ? "La base es mayor" : "La altura es mayor";
System.out.println("Operador T: "+ operadorT);       
    }
         
}
