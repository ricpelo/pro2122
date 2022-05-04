package personas;

public class Cliente {
    private static long numClientes;

    private String dni;
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

    // public String toString() {
    // }

    public long getNumero() {
        return numero;
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
}
