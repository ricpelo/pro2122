package personas;

import java.util.Objects;

import interfaces.Numerable;

public abstract class Cliente implements Numerable {
    private static long numClientes;

    protected String dni;
    private String nombre;
    private final long numero;

    public Cliente(String dni, String nombre) {
        setDni(dni);
        setNombre(nombre);
        Cliente.numClientes++;
        numero = numClientes;
    }

    public static long getNumClientes() {
        return Cliente.numClientes;
    }

    public static String pintarBonito(String dni, String nombre) {
        // return String.format("(%s) %s", dni, nombre);
        return "(" + dni + ") " + nombre;
    }

    @Override
    public String toString() {
        return String.format("(%s) %s", dni, nombre);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }

        if (obj == null) {
            return false;
        }

        if (getClass() != obj.getClass()) {
            return false;
        }

        Cliente otro = (Cliente) obj;

        return numero == otro.getNumero();
    }

    @Override
    public int hashCode() {
        return Objects.hash(numero);
    }

    @Override
    public long getNumero() {
        return numero;
    }

    public String getDni() {
        return dni;
    }

    public final void setDni(String dni) {
        this.dni = dni;
    }

    public String getNombre() {
        return nombre;
    }

    public final void setNombre(String nombre) {
        this.nombre = nombre;
    }
}
