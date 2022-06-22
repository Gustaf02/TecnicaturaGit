
package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("Digite el nombre del libro");
        String nombreLibro = entrada.nextLine();

        System.out.println("Digite el id del libro");
        int idLibro = Integer.parseInt(entrada.nextLine());

        System.out.println("Digite el precio del libro");
        double precioLibro = Double.parseDouble(entrada.nextLine());

        System.out.println("Confirme si el envío es gratuito");
        boolean envioGratuito = Boolean.parseBoolean(entrada.nextLine());

        System.out.println("nombre del libro " + idLibro);
        System.out.println("precio del libro " + precioLibro);
        System.out.println("el envío del libro es gratuito " + envioGratuito);

    }
           
}
