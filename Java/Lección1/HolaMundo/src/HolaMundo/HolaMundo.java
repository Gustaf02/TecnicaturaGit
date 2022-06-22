package HolaMundo;

public class HolaMundo {

    public static void main(String[] args) {
        /*System.out.print("Hola mundo desde Java");

        int miVariable = 10;

        System.out.println(miVariable);

        miVariable = 5;
// Tipo String 
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Seguimos aprendiendo en programación";
        System.out.println(miVariableCadena);
        //Inferencia de tipos en Java
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2= " + miVariableEntera2);
        System.out.println("miVariableCadena2= " + miVariableCadena2);
        //soutv + tab
        // Tecla Shitf + F6 es la tecla para mayúscula
        // Reglas para definir una variable en Java*/

        /*var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("unión= " + union);
        // Control s se guarda el código
        // botón derecho y format ordena el texto

       var a = 8;
       var b = 4;
       System.out.println(usuario+ " " + (a+b));
   
       // Ejercicio caracteres especiales con Java   
       var nombre = "Natalia";
        System.out.println("\nNueva Línea: \n" + nombre); //Diagonal inversa + n
        System.out.println("Tabulador: \t" + nombre);//sirve para centrar
        System.out.println("\t \t.:Menú:.");
        System.out.println("Retroceso: \b\b"+ nombre);//caracter de retroceso
        System.out.println("Comillas simples: \'" + nombre + "\'");
        System.out.println("Comillas dobles: \"" + nombre + "\" ");*/
        //Clase Scanner
        /* Scanner entrada = new Scanner(System.in);
        var usuario2 = "Carlos";
        System.out.println("Usuario2 = " + usuario2); */
        //Clase Scanner
        /* Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre ");
        var usuario2 = entrada.nextLine();
        System.out.println("Usuario2 = " + usuario2);
        System.out.println("Escriba la profesión ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado "+ titulo2+ " " + usuario2); */
 /*byte numEnteroByte = 127;
        System.out.println("numEnteroByte = "+ numEnteroByte);
        System.out.println(" Valor mínimo del byte: "+ Byte.MIN_VALUE);
        System.out.println("Valor máximo del byte: "+ Byte.MAX_VALUE );
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort =  "+numEnteroShort);
        System.out.println("Valor mínimo del short: "+ Short.MIN_VALUE);
        System.out.println("Valor máximo del short: "+ Short.MIN_VALUE);
        
        int numEnteroInt = (int)2147403648L;
        System.out.println("numEnteroInt =  "+numEnteroInt);
        System.out.println("Valor mínimo del int: "+ Integer.MIN_VALUE);
        System.out.println("Valor máximo del int: "+ Integer.MIN_VALUE);
        
        long numEnteroLong = 10;
        System.out.println("numEnteroLong =  "+numEnteroLong);
        System.out.println("Valor mínimo del long: "+ Long.MIN_VALUE);
        System.out.println("Valor máximo del long: "+ Long.MIN_VALUE);
        
        float numEnteroFloat = 3.4028235E38F; 
        System.out.println("numFloat =  "+numEnteroFloat);
        System.out.println("Valor mínimo del float: "+ Float.MIN_VALUE);
        System.out.println("Valor máximo del float: "+ Float.MIN_VALUE);
        
        double numDouble = 1.7976931348623157E308D; 
        System.out.println("numDouble =  "+numDouble);
        System.out.println("Valor mínimo del double: "+ Double.MIN_VALUE);
        System.out.println("Valor máximo del double: "+ Double.MIN_VALUE);*/
        //inferencia de tipo var y tipos primitivos
        /*var numEntero = 20;
        System.out.println("numEntero = "+ numEntero);
        var numFloat = 10.0F; //automáticamente con el punto se transforma
        System.out.println("numFloat"+ numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble"+ numDouble);
        
        //Tipo primitivo char
        char miVariableChar = 'a'; // se usa ' 
        System.out.println("miVariableChar = "+miVariableChar );*/
 /*char varCaracter = '\u0024'; // Indicamos a java la asignación con el código unicode
        System.out.println("varCaracter  = "+varCaracter);
        char varCaracterDecimal = 36; // Valor decimal del juego de caracter unicode
        System.out.println("varCaracterDecimal = "+varCaracterDecimal);
        char varCaracterSimbolo = '$'; // un caracter especial podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = "+varCaracterSimbolo);
        
        char varCaracter1 = '\u0024'; // Indicamos a java la asignación con el código unicode
        System.out.println("varCaracter1  = "+varCaracter);
        char varCaracterDecimal1 = 36; // Valor entero y le asigna un tipo int
        System.out.println("varCaracterDecimal1 = "+varCaracterDecimal1);
        char varCaracterSimbolo1 = '$'; // un caracter especial podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = "+varCaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar"+varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar"+caracterChar);*/
        //tipo primitivo tipo booleano
        /* var varBbool = false;
        System.out.println("varBool: "+ varBbool ); 
        
        if (varBbool){
            System.out.println("La bandera es verde");
        }
        else {
            System.out.println("La bandera es roja");
        }
        
        // Algoritmo es mayor de edad
        var edad =30; //literal tiene preeente la inferencia de tipos
        var adulto = edad >=18; //esta es una expresión booleana
        if (adulto){
            System.out.println("Eres mayor de edad");
        }
        else {
            System.out.println("Eres menor de edad");
        }*/
        //Conversión de tipo primitivo
        /*var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad+1));
        var valorPi = Double.parseDouble("3.1416");
        System.out.println("Valor Pi: "+ valorPi);
        
        //Pedir un valor
        var entrada = new Scanner(System.in);
        System.out.println("Digite su edad");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("Edad:    "+edad);
        //conversión de tipo primitivo en java 2: de entero a String
        /*var entrada = new Scanner(System.in);*
        
        var edadTexto = String.valueOf(10); 
        System.out.println("edad texto " + edadTexto);
        
        var fraseChar = "programadores".charAt(10); 
        System.out.println("fraseChar " + fraseChar);
        
        System.out.println("Digite un caracter ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar" + fraseChar);*/
        
        /*int num1 = 5, num2 =4;
        var solucion = num1 + num2;
        System.out.println("Solución de la suma: " + solucion);
        
        solucion = num1 - num2;
        System.out.println("Solución de la resta: " + solucion);
        
        solucion = num1 * num2;
        System.out.println("Solución de la multiplicación: " + solucion);
        
        solucion = num1 / num2;
        System.out.println("Solución de la división: " + solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("Solución 2 de la divión: "+ solucion2);
        
        solucion = num1 % num2; //guarda el residuo entero de la división
        System.out.print("Solución" + solucion);
        
        if (num1 % 2 == 0)
        
            System.out.println("Es número par");
        
        else 
            System.out.println("Es número impar");*/
 /*int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2; // una operación
        System.out.println("varNum3 = "+ varNum3);
        
        varNum1 += 1;
        System.out.println("varNum1 = " + varNum1);
        
         varNum1 -= 2;
        System.out.println("varNum2 = " + varNum2);
        
         varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
        
         varNum1 /= 4;
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 %= 6;
        System.out.println("varNum1 = " + varNum1);*/
        //operadores unarios
        /*var varA = 7;
        var varB = -varA;
        System.out.println("varA = "+ varA);
        System.out.println("varB = "+ varB);//el resultado será un número negativo
        
        //operador de negación
        var varC = true;
        var varD = !varC;
        System.out.println("varC = "+ varC);
        System.out.println("varD = "+ varD);
       
        //Operadores unarios de incremento: Preincremento
        var varE = 9;//se va a modificar su valor
        var varF = ++varE;//Símbolo antes de la variable
        //Primero se incrementa la variable y después se usa su valor
        System.out.println("varE = "+ varE);//se incrementa en la unidad
        System.out.println("varF = "+ varF);//va a sumar 1
        
        //Post incremento. El símbolo va después de la variable. 
        
        var varG= 3;//primero el valor de la variable, luego el incremento. 
        var varH = varG++;
        System.out.println("varG = "+ varG);//se incrementa en la unidad
        System.out.println("varH = "+ varH);
        
        //Operadores unarios de decremento
        var varI= 4;//primero el valor de la variable, luego el decremento. 
        var varJ = --varI;
        System.out.println("varI = "+ varI);
        System.out.println("varJ = "+ varJ);
        
        //Post decremento
        var varK= 8;//primero el valor de la variable, luego el decremento. 
        var varL = varK--;
        System.out.println("varK = "+ varK);
        System.out.println("varL = "+ varL);*/
        //operadores de igualdad y relacionales
        /*var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum= "+ cNum);
        
        var dNum = aNum != bNum;
        System.out.println("dNum= "+ dNum);
        
        var cadenaA = "Hello";
        var cadenaB = "bye bye";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar= "+ cVar);
        
        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar " + fVar);
        
        var gVar = aNum != bNum; //> >= < <= != ==
        System.out.println("gVar= "+ gVar);
        
        if(aNum % 2 == 0){
            System.out.println("El número es par");}
        else{ 
            System.out.println("El número es impar");}*/
        //Operador condicional and
        /*var valorA = 7;
        var valorMinimo = 0;
        var valorMaximo =10;
        var respuesta = valorA >= 0 && valorA  <=10;
        
        if (respuesta)
            System.out.println("Está dentro del rango establecido");
        else
            System.out.println("No está dentro del rango establecido");
        
        
        var vacaciones = false;
        var diaLibre = true;
        
        if (vacaciones || diaLibre)
            System.out.println("Papá puede asistir al juego de su hijo");
        else
            System.out.println("Papá no puede asistir al juego de su hijo");*/
        //Operador ternario
        /* var resultadoT = (5 > 8)? "Verdadero" : "False";
        System.out.println("resultadoT = " + resultadoT );
        
        var numeroT = 4;
        resultadoT = (numeroT % 2 == 0)? "Es par" : "Es impar";
        System.out.println("resultadoT = " + resultadoT);*/
        //Prioridad de los operadores
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x= " + x);
        System.out.println("y= " + y);
        System.out.println("z= " + z);

        var solucionAritmetica = 4 + 5 * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);

        solucionAritmetica = (4 + 5) * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);

    }
}
