/*
 
 */
package domain;


public class Empleado extends Persona {
    private int idempleado;
    private double sueldo;
    private static int contadorEmpleado; // es para incrementar
    
    // Constructor
    
    public Empleado(){   // Constructor 1
        this.idempleado = ++Empleado.contadorEmpleado;
    }

    public Empleado(String nombre, double sueldo) { // Constructor 2
        // super(nombre);            super llama al constructor de la clase padre
        this();      // Se llama al constructor vacío (al constructor interno). Se usa super o this. No ambos.
        this.nombre = nombre;  
        this.sueldo = sueldo;
    }

    public int getIdempleado() {
        return this.idempleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{idempleado=").append(idempleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
                 
        
}
