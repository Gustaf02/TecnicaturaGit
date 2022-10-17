/*

 */
package dominio;

public class Persona {
    //atributos
    private String nombre; //usamos modificador de acceso private
    private double sueldo; //estos atributos están encapsulados
    private boolean eliminado; 

    //Constructor
    public Persona(String nombre, double sueldo, boolean eliminado){
        this.nombre = nombre; //el this identifia
        this.sueldo = sueldo; //al atributo de la variable
        this.eliminado = eliminado; 
    }
    //Métodos getter y setter
    //Necesitamos un getter y un setter por cada atributo 

    //Getter para atributo nombre
    public String getNombre(){
        return nombre;
    }

    //setter para atributo nombre
    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    //getter para atributo sueldo
    public double getSueldo(){
        return sueldo;
    }

    //setter para atributo sueldo
    public void setSueldo(double sueldo){
        this.sueldo = sueldo;
    }

    //getter para atributo eliminado
    public boolean isEliminado(){ //en boolean se usa el 'is' no el get
        return eliminado;
    }

    //setter para atributo eliminado
    public void setEliminado(boolean eliminado){
        this.eliminado = eliminado;
    }
}
    

