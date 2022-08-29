package ciclowhile;


public class EjercicioWhile01 {
    
    public static void main(String[] args) {
// Ciclo while
        var conteo = 0;  // Interferencia de tipos
        while (conteo < 3){
            System.out.println("conteo" + conteo );
            conteo ++; // Vamos aumentando en uno la variable
        }
// Ciclo do while
        
        var contador = 0;
        do{
            System.out.println("contador" + contador);
            contador ++;
          }while(contador<7);
        
// Ciclo for se puede colocar for (int i =0; ....). En este caso usaremos var

/*for (var contando=0; contando<7; contando++){
        System.out.println("contando"+ contando);
    }
       */
// Vemos acá el break 
for (var contando=0; contando<7; contando++){
    if (contando%2==0){
        System.out.println("contando"+ contando);
        break; // si no coloco el break me muestra 0,2,4,6. Al colocar el break se detiene en 0 (múlt. 2)
    } 
}   
// Vemos ahora el continue
    for (var contando=0; contando<7; contando++){
    if (contando%2!=0){  //diferente de 0
        
        continue; // vamos a la siguiente iteración. Continúa cuando ve un número impar. Imprime pares
    } 
    System.out.println("contando"+ contando);
    
    /* uso de etiquetas label. No es recomendable su uso, pero es necesario conocerlo. Hace lo mismo. 
    inicio:
    for (var contando=0; contando<7; contando++){
    if (contando%2==0){
        System.out.println("contando"+ contando);
        break inicio; // si no coloco el break me muestra 0,2,4,6. Al colocar el break se detiene en 0 (múlt. 2)
    } // Se pueden usar con el break y con el continue*/
}   
    
}
    }

