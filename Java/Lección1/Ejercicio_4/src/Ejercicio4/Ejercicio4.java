
package Ejercicio4;

import java.util.Scanner;

public class Ejercicio4 {
    
     public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
 System.out.println("Digite un número: ");
int num1 = Integer.parseInt(entrada.nextLine());
System.out.println("Digite un segundo número");
int num2 = Integer.parseInt(entrada.nextLine());

//vamos ahora cuál número es mayor
var operadorT= (num1> num2) ? "num1 es mayor" : "num2 es mayor";
System.out.println("operadorT " + operadorT);
     
        
        
    }
   
   
}
