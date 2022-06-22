
package Ejercicio2;

import java.util.Scanner;


public class Ejercicio2 {
    public static void main(String[] args) {
    
   Scanner entrada= new Scanner(System.in);
System.out.println("¿Cuánto es el sueldo por hora del empleado");
int sueldoHora = Integer.parseInt(entrada.nextLine());

System.out.println("¿Cuántas horas trabajó");
int horasTrabajadas = Integer.parseInt(entrada.nextLine());

int sueldo = sueldoHora * horasTrabajadas;

    System.out.println("El sueldo del empleado es "+ sueldo);

    }
    
       
    
}
