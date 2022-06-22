package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {

    public static void main(String[] args) {

        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un mes del año: ");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "Estacion desconocida";
        if (mes == 1 || mes == 2 || mes == 3) {
            estacion = "Verano";
        } else if (mes == 4 || mes == 5 || mes == 6) {
            estacion = "Verano";
        } else if (mes == 7 || mes == 8 || mes == 9) {
            estacion = "Verano";
        }
        if (mes == 10 || mes == 11 || mes == 12) {
            estacion = "Primavera";
        }
        System.out.println("Estación:  " + estacion);*/
        Scanner entrada = new Scanner(System.in);

        var numero = 2;
        var numeroTexto = "Valor desconocido";
        switch (numero) {
            case 1:
                numeroTexto = "Número uno";
                break;
            case 2:
                numeroTexto = "Número dos";
                break;

            case 3:
                numeroTexto = "Número tres";
                break;

            case 4:
                numeroTexto = "Número cuatro";
                break;
            default:
                numeroTexto = "Caso no encontrado";
        }

        System.out.println("Número texto: " + numeroTexto);

    }

}
