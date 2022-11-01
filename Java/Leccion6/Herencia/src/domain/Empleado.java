/*
 
 */
package domain;


public class Empleado extends Persona {
    private int idempleado;
    private double sueldo;
    private static int contadorEmpleado; // es para incrementar
    
    // Constructor

    public Empleado(String nombre, double sueldo) {
        super(nombre);
        this.idempleado = ++Empleado.contadorEmpleado;
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
