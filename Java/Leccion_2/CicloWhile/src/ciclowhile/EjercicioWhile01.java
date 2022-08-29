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

for (var contando=0; contando<7; contando++){
        System.out.println("contando"+ contando);
    }
    
   } 
           
}

