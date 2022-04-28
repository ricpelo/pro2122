package personas;

public class Cliente {
    private String dni;
    private String nombre;

    public Cliente(String dni, String nombre) {
        setDni(dni);
        setNombre(nombre);
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
