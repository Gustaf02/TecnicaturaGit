
package Ejercicio7;

import java.util.Scanner;


public class Ejercicio7 {
    public static void main(String[] args) {
        final int salario =1000;
  Scanner entrada= new Scanner(System.in);      
int comision=150, venta;
float salarioMensual, ventaCarro, porcVenta, totalPrecio;

System.out.print("Digite la cantidad de carros vendidos: ");
venta = Integer.parseInt(entrada.nextLine());

System.out.print("Digite el precio de un carro: ");
ventaCarro= Float.parseFloat(entrada.nextLine());

comision += venta;

totalPrecio = ventaCarro + venta;

porcVenta =totalPrecio * 0.05f;
salarioMensual=salario+comision+porcVenta;
System.out.print("\nMi salario mensual es: " +  salarioMensual);    
        
     }
     
 }
